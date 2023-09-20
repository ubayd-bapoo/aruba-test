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
