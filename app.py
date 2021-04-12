from src.location import Location

l = Location()

# Optional
l.refresh_locations()

username = input("Enter username: ")
location = l.search(username)
print(location)
