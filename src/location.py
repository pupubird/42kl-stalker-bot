from dotenv import load_dotenv
import requests
import json
import os

load_dotenv()


class Location:
    def __init__(self):
        self.client_id = os.getenv('CLIENT_ID_42')
        self.client_secret = os.getenv('CLIENT_SECRET_42')
        self._get_location()

    def refresh_locations(self):
        print("Updating user's location data")
        res = requests.post(
            "https://api.intra.42.fr/oauth/token",
            data={
                "grant_type": "client_credentials",
                "client_id": self.client_id,
                "client_secret": self.client_secret,
            },
        )

        access_token = res.json()["access_token"]

        locations = requests.get(
            f"https://api.intra.42.fr/v2/campus/34/locations/",
            headers={"Authorization": f"Bearer {access_token}"},
        ).json()

        self.locations = list(filter(lambda x: x["end_at"] == None, locations))

        for location in self.locations:
            del location["id"]
            del location["primary"]
            del location["campus_id"]
            location["user_id"] = location["user"]["login"]
            del location["user"]
        os.makedirs('data', exist_ok=True)
        with open("data/locations.json", 'w') as f:
            f.writelines(json.dumps(self.locations, indent=2))
        return self.locations

    def resolve_location(self, host):
        area = host[0:3]
        zone = host[3:6]
        if area == "u80":
            if zone == "z01" or zone == "z03" or zone == "z05":
                return ("I am around downstairs behind Thila table!")
            if zone == "z04" or zone == "z02":
                return ("I am around upstairs behind office!")
        if area == "u81":
            if zone == "z01" or zone == "z03" or zone == "z05":
                return ("I am around downstairs drinking station!")
            if zone == "z02" or zone == "z04":
                return ("I am around upstairs near to the stairs!")
            if zone == "z06" or zone == "z08":
                return ("I am around upstairs drinking station!")
        if area == "u82":
            if zone == "z01" or zone == "z03" or zone == "z05":
                return ("I am around downstairs kitchen area!")
            if zone == "z02" or zone == "z04" or zone == "z06" or zone == "z08":
                return ("I am around upstairs near male toilet!")
        return ""

    def search(self, username):
        if not self.locations:
            self.refresh_locations()
        for location in self.locations:
            if username == location["user_id"]:
                return self.resolve_location(location["host"])
        else:
            return None

    def _get_location(self):
        try:
            with open("data/locations.json", 'r') as f:
                self.locations = json.load(f)
        except FileNotFoundError:
            self.refresh_locations()


if __name__ == "__main__":
    username = input("Enter username: ")
    l = Location()
    location = l.search(username)
    print(location)
