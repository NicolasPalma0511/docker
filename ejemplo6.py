from geopy.geocoders import Nominatim
from geopy.distance import geodesic

geolocator = Nominatim(user_agent="geoapiExercises")

ubicacion1 = geolocator.geocode("1600 Amphitheatre Parkway, Mountain View, CA")
ubicacion2 = geolocator.geocode("1 Infinite Loop, Cupertino, CA")

coord_ubicacion1 = (ubicacion1.latitude, ubicacion1.longitude)
coord_ubicacion2 = (ubicacion2.latitude, ubicacion2.longitude)

print(f"Ubicación 1 (Google HQ): {coord_ubicacion1}")
print(f"Ubicación 2 (Apple HQ): {coord_ubicacion2}")

distancia = geodesic(coord_ubicacion1, coord_ubicacion2).kilometers
print(f"Distancia entre las dos ubicaciones: {distancia:.2f} km")
