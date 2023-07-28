arr = [2,2,2]
cont = 1
for x in arr:
    if x < arr[cont]:
        x += 1
        print(x)















'''
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="app-prueba")
# location = geolocator.geocode("856 Smith St RI")
# location = geolocator.geocode("Colon - Temoaya, Avenida 20 de Noviembre, San Cristóbal, San Andres Coexcotitlan, Toluca, Estado de México, 50200, México")
location = geolocator.geocode("3, c/ restauracion, san cristobal, DO")
#location = geolocator.geocode("hospital princeton PLAINSBORO NJ")
print(location.address)
print("--------------")
print((location.latitude, location.longitude))
print("--------------")
print(('Hola', 'Mundo', 'Cruel'))
print(location.raw)
print("--------------")
'''