import unittest

from app import app


class TestAPI(unittest.TestCase):
    def setUp(self) -> None:
        self.app = app.test_client()
        self.app.testing = True

    def test_get_info(self):
        response = self.app.get("/api/info")
        data = {
            "info": {
                "asins": [
                    "B00099E8WI",
                    "B00099E91I",
                    "B00099E922",
                    "B00099XNVA",
                    "B0009ET8VO",
                ],
                "brand_names": [
                    "AKEfit",
                    "Arm & Hammer",
                    "Beautys 101",
                    "Black Duck Brand",
                    "Bounce",
                    "Brio Living",
                    "Budieggs",
                    "Calgon",
                    "CompuClever",
                    "Downy",
                    "Friendsheep",
                    "Gain",
                    "Grab Green",
                    "Handy Laundry",
                    "Heart Felt",
                    "KINTOR",
                    "MRS. MEYER'S CLEAN DAY",
                    "Method",
                    "OHOCO",
                    "Pure Homemaker",
                    "Purex",
                    "S&T INC.",
                    "SUN",
                    "SUPA MODERN",
                    "Seventh Generation",
                    "Snuggle",
                    "Suavitel",
                    "Whitmor",
                    "Woolous",
                    "Woolzies",
                ],
                "earliest_date": "2007-01-03",
                "ids": [
                    "R1005KDSAFSTCQ",
                    "R100BR7970301Q",
                    "R100GD1Q6QGLBF",
                    "R100LP5HTVX7J0",
                    "R100MCDRDX1IMN",
                ],
                "latest_date": "2020-07-02",
                "sources": ["amazon"],
                "stars": [1, 2, 3, 4, 5],
            }
        }

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, data)

    def test_get_timeline_with_no_required_params(self):
        response = self.app.get("/api/timeline")
        data = {
            "errors": {
                "Grouping": ["This field is required."],
                "Type": ["This field is required."],
                "endDate": ["This field is required."],
                "startDate": ["This field is required."],
            }
        }
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, data)

    def test_get_timeline_with_invalid_params(self):
        response = self.app.get(
            "/api/timeline?startDate=2020-01-01&endDate=2020-01-01&Grouping=brand&Type=invalid"
        )
        data = {
            "errors": {
                "Grouping": ["Not a valid choice."],
                "Type": ["Not a valid choice."],
            }
        }
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, data)

    def test_get_timeline_with_valid_params_usual(self):
        response = self.app.get(
            "/api/timeline?startDate=2020-01-01&endDate=2020-01-15&Grouping=monthly&Type=usual"
        )
        data = {
            "timeline": [
                {"date": "2020-01-07", "value": 40},
                {"date": "2020-01-05", "value": 27},
                {"date": "2020-01-10", "value": 37},
                {"date": "2020-01-01", "value": 47},
                {"date": "2020-01-02", "value": 31},
                {"date": "2020-01-09", "value": 35},
                {"date": "2020-01-12", "value": 35},
                {"date": "2020-01-13", "value": 49},
                {"date": "2020-01-03", "value": 46},
                {"date": "2020-01-14", "value": 36},
                {"date": "2020-01-08", "value": 33},
                {"date": "2020-01-06", "value": 43},
                {"date": "2020-01-04", "value": 54},
                {"date": "2020-01-15", "value": 22},
                {"date": "2020-01-11", "value": 52},
            ]
        }
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, data)

    def test_get_timeline_with_valid_params_cumulative(self):
        response = self.app.get(
            "/api/timeline?startDate=2019-01-01&endDate=2019-01-15&Grouping=monthly&Type=cumulative"
        )
        data = {
            "timeline": [
                {"date": "2019-01-02", "values": 16},
                {"date": "2019-01-11", "values": 36},
                {"date": "2019-01-13", "values": 65},
                {"date": "2019-01-08", "values": 79},
                {"date": "2019-01-12", "values": 109},
                {"date": "2019-01-03", "values": 124},
                {"date": "2019-01-15", "values": 142},
                {"date": "2019-01-05", "values": 158},
                {"date": "2019-01-07", "values": 181},
                {"date": "2019-01-09", "values": 195},
                {"date": "2019-01-01", "values": 210},
                {"date": "2019-01-14", "values": 233},
                {"date": "2019-01-04", "values": 251},
                {"date": "2019-01-06", "values": 271},
                {"date": "2019-01-10", "values": 288},
            ]
        }
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, data)

    def test_get_timeline_with_filtering(self):
        response = self.app.get(
            "/api/timeline?startDate=2019-01-01&endDate=2019-01-15&Grouping=monthly&Type=cumulative&brand=Gain"
        )
        data = {
            "timeline": [
                {"date": "2019-01-05", "values": 1},
                {"date": "2019-01-08", "values": 2},
                {"date": "2019-01-10", "values": 3},
                {"date": "2019-01-11", "values": 4},
                {"date": "2019-01-14", "values": 5},
            ]
        }
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, data)
