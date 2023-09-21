import os
import time
import hashlib
import logging
import requests

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from service_app.models.access_point import AccessPoint, Response


router = APIRouter()

# All variable that only needs to be called once
URL = 'https://www.googleapis.com/geolocation/v1/geolocate'
HEADERS = {
    'Content-Type': 'application/json',
}
PARAMS = {
    'key': os.environ.get('KEY'),
}

# Define the cache data structure
CACHE = {}
CACHE_EXPIRY_TIME = 5 * 60  # 15 minutes in seconds, we expire the cache without needing to restart the service


@router.post("/api/v1/geolocation/",
             tags=["Geolocation"],
             description="This endpoint is used to received a list of access points to be sent to Google.",
             response_model=Response
             )
def read_root(access_points: list[AccessPoint]):
    if len(access_points) < 2:
        # Per Googles docs https://developers.google.com/maps/documentation/geolocation/intro
        return JSONResponse(
            status_code=400,
            content={"error": "Custom Error", "detail": "Require minimum of 2 access points"},
        )

    data = {
      "considerIp": "false",
      "wifiAccessPoints": []
    }

    bssids = set()
    for ap in access_points:
        data["wifiAccessPoints"].append({
            "macAddress": ap.bssid,
            "signalStrength": ap.rssi,
            "signalToNoiseRatio": 0,
            "channel": ap.channel,
        })
        bssids.add(ap.bssid)

    # Keeping the set sorted so that we always get the same key, when we get the same access_points in a different order
    unique_key = hashlib.sha256(''.join(sorted(bssids)).encode()).hexdigest()
    if unique_key in CACHE:
        logging.info('Retrieved from cache')
        cached_result, timestamp = CACHE[unique_key]
        current_time = time.time()

        # Check if the cache entry is still valid
        if current_time - timestamp <= CACHE_EXPIRY_TIME:
            return cached_result
        logging.info('Cache expired')

    logging.info('Sending request to Google')
    response = requests.post(URL, params=PARAMS, headers=HEADERS, json=data)
    if not response.status_code == 200:
        logging.error('Error sending request to Google')
        clean_json = response.json()['error']
        return JSONResponse(
            status_code=clean_json['code'],
            content={"error": "Custom Error",
                     "detail": f"Error with response to Google: {clean_json['message']}"},
        )

    CACHE[unique_key] = (response.json(), time.time())
    return response.json()
