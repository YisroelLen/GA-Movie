import geocoder
import requests

API_BASE_URL = "https://api.darksky.net/forecast/[YOUR_API_KEY_HERE]/"
degree_sign= u'\N{DEGREE SIGN}'

destinations = ["Space Needle",
"Crater Lake",
"Golden Gate Bridge",
"Yosemite National Park",
"Las Vegas, Nevada",
"Grand Canyon National Park",
"Aspen, Colorado",
"Mount Rushmore",
"Yellowstone National Park",
"Sandpoint, Idaho",
"Banff National Park",
"Capilano Suspension Bridge",]

for place in destinations:
  g = geocoder.arcgis(place)
  lat_and_lon = g.latlng
  lat = lat_and_lon[0]
  lon = lat_and_lon[1]
  API_BASE_URL = "https://api.darksky.net/forecast/MyAPIKey/"
  full_api_url = API_BASE_URL + str(lat) + "," + str(lon) + "?exclude=minutely,hourly,daily,alerts,flags"
  result = requests.request('GET', full_api_url).json()
  print (place + " is located at " + "{0:.2f}" ", " "{1:.2f}".format(lat, lon))
  print ("At the {0} right now, it's {1} with a temperature of {2}{3}f.\n ".format(place, result['currently']['summary'], result['currently']['temperature'],degree_sign))
  print ("Powered by Dark Sky")
