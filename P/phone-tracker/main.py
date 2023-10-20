import phonenumbers
import opencage
import folium


from phone import number
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode


pepnumber = phonenumbers.parse(number)

location = geocoder.description_for_number(pepnumber, "en")


print(location)


service_pro = phonenumbers.parse(number)

print(carrier.name_for_number(service_pro,"en"))


key = '' # Put your API key here 

geocoder = OpenCageGeocode(key)

query = str(location)

results = geocoder.geocode(query)


print(results)

if results:
    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']
    print(lat, lng)
else:
    print("No results found.")


myMap = folium.Map(location=[lat,lng], zoom_start = 9)
folium.Marker([lat,lng], popup = location).add_to(myMap)


myMap.save("myLocation.html")