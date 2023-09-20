import os
import logging
import requests

from fastapi import APIRouter

from service_app.models.access_point import AccessPoint

router = APIRouter()
URL = 'https://www.googleapis.com/geolocation/v1/geolocate'
HEADERS = {
    'Content-Type': 'application/json',
}
PARAMS = {
    'key': os.environ.get('KEY'),
}


@router.post("/api/v1/geolocation/")
def read_root(access_points: list[AccessPoint]):
    data = {
      "considerIp": "false",
      "wifiAccessPoints": []
    }

    for ap in access_points:
        data["wifiAccessPoints"].append({
            "macAddress": ap.bssid,
            "signalStrength": ap.rssi,
            "signalToNoiseRatio": 0,
            "channel": ap.channel,
        })

    logging.info('Sending request to Google')
    response = requests.post(URL, params=PARAMS, headers=HEADERS, json=data)
    return response.json()
