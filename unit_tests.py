import unittest

from fastapi.testclient import TestClient
from service import app
from service_app.routers import RouterRegister


class TestMain(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(app)
        RouterRegister.register(app)

    def test_read_root(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 404)

    def test_read_healthcheck(self):
        response = self.client.get("/meta/health")
        self.assertEqual(response.status_code, 200)

    def test_post_one_ap(self):
        data = [
            {
                "band": "2.4",
                "bssid": "f4:2e:7f:30:3e:50",
                "channel": "5",
                "frequency": 5500,
                "rates": "1.0 - 135.0 Mbps",
                "rssi": -38,
                "security": "wpa-psk",
                "ssid": "hpe",
                "timestamp": 1693830969.468209,
                "vendor": "HUAWEI TECHNOLOGIES CO.,LTD",
                "width": "20"
            }
        ]
        response = self.client.post("/api/v1/geolocation/", json=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'error': 'Custom Error', 'detail': 'Require minimum of 2 access points'})

    def test_post_multiple_ap_no_key(self):
        data = [
            {
                "band": "2.4",
                "bssid": "f4:2e:7f:30:3e:50",
                "channel": "5",
                "frequency": 5500,
                "rates": "1.0 - 135.0 Mbps",
                "rssi": -38,
                "security": "wpa-psk",
                "ssid": "hpe",
                "timestamp": 1693830969.468209,
                "vendor": "HUAWEI TECHNOLOGIES CO.,LTD",
                "width": "20"
            },
            {
                "band": "2.4",
                "bssid": "f4:2e:7f:30:3e:52",
                "channel": "5",
                "frequency": 5500,
                "rates": "1.0 - 135.0 Mbps",
                "rssi": -38,
                "security": "wpa-psk",
                "ssid": "ethersphere-wpa2",
                "timestamp": 1693830969.487669,
                "vendor": "HUAWEI TECHNOLOGIES CO.,LTD",
                "width": "20"
            },
            {
                "band": "2.4",
                "bssid": "64:d1:54:91:07:8e",
                "channel": "5",
                "frequency": 5660,
                "rates": "1.0 - 135.0 Mbps",
                "rssi": -46,
                "security": "wpa-psk",
                "ssid": "Healthbridge",
                "timestamp": 1693830970.507561,
                "vendor": "HUAWEI TECHNOLOGIES CO.,LTD",
                "width": "20"
            }

        ]
        response = self.client.post("/api/v1/geolocation/", json=data)
        self.assertEqual(response.status_code, 403)


if __name__ == "__main__":
    unittest.main()
