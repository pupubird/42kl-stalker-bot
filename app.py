from src.location import Location

username = input("Enter username: ")
l = Location()
location = l.search(username)
print(location)
