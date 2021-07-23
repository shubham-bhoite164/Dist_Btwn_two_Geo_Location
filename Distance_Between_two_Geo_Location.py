# pip install geopy
# pip install geocoders

from geopy.geocoders import Nominatim
from geopy import distance

a = Nominatim(user_agent = "Shubham")
place_1 = input("Please enter your first location")
place_2 = input("Please enter your second location")

destination_1 = a.geocode(place_1)
destination_2 = a.geocode(place_2)

lat_1 , long_1 = (destination_1.latitude), (destination_1.longitude)          # Latitude and Longitude
lat_2 , long_2 = (destination_2.latitude), (destination_2.longitude)

lenght_1 = (lat_1,long_1)
lenght_2 = (lat_2,long_2)

print(f'The Distance between {place_1} and {place_2} is {distance.distance(lenght_1, lenght_2)}')