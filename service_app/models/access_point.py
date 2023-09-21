from pydantic import BaseModel


class AccessPoint(BaseModel):
    band: float
    bssid: str
    channel: int
    frequency: int
    rates: str
    rssi: int
    security: str
    ssid: str
    timestamp: float
    vendor: str
    width: int


class GeoLocation(BaseModel):
    lat: float
    lng: float


class Response(BaseModel):
    location: GeoLocation
    accuracy: float