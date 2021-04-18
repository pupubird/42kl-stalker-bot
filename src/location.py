from dotenv import load_dotenv
import requests
import json
import os

load_dotenv()


class Location:
    def __init__(self):
        self.client_id = os.getenv("CLIENT_ID_42")
        self.client_secret = os.getenv("CLIENT_SECRET_42")
        self.locations = []
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

        os.makedirs("data", exist_ok=True)
        for location in self.locations:
            del location["id"]
            del location["primary"]
            del location["campus_id"]
            location["user_id"] = location["user"]["login"]
            del location["user"]
        with open("data/locations.json", "w") as f:
            print("Saving locations to file")
            f.writelines(
                json.dumps(
                    self.locations if len(self.locations) > 0 else None, indent=2
                )
            )
        return self.locations

    def resolve_location(self, host):
        area = host[0:3]
        zone = host[3:6]
        with open("reference.json", "r") as f:
            references = json.load(f)
            area_ref = references.get(area, None)
            if area_ref:
                return area_ref[zone]
        return ""

    def search(self, username):
        if not self.locations:
            self.refresh_locations()
        if len(self.locations) == 0:
            return None
        for location in self.locations:
            if username == location["user_id"]:
                return self.resolve_location(location["host"])
        else:
            return None

    def _get_location(self):
        try:
            with open("data/locations.json", "r") as f:
                print("Locations loaded from file")
                self.locations = json.load(f)
        except FileNotFoundError:
            print("File not found")
            self.refresh_locations()


if __name__ == "__main__":
    username = input("Enter username: ")
    l = Location()
    location = l.search(username)
    print(location)
