#
# Get the weather XML, parse and return it back as a JSON string
# Example XML page: http://api.wunderground.com/auto/wui/geo/WXCurrentObXML/index.xml?query=90210
#
# (c) 2016 Pat O'Brien - http://obrienlabs.net
# Licensed under the MIT License. Please include original copyright string in any new works.
#

import sys, untangle

zip = sys.argv[1]
xml = untangle.parse("http://api.wunderground.com/auto/wui/geo/WXCurrentObXML/index.xml?query=%s" % zip)

updated = xml.current_observation.observation_time.cdata
city = xml.current_observation.display_location.full.cdata
temp = xml.current_observation.temperature_string.cdata
humidity = xml.current_observation.relative_humidity.cdata
dewpoint = xml.current_observation.dewpoint_string.cdata
wind = xml.current_observation.wind_string.cdata
pressure = xml.current_observation.pressure_string.cdata
conditions = xml.current_observation.weather.cdata

# Check to make sure we have a valid location by seeing if there is temperature data
if ( xml.current_observation.temp_f.cdata is None or xml.current_observation.temp_f.cdata == "" ):
    output = "Error: %s is an invalid location, or there was an error fetching data from wunderground.com." % zip
else:
    output = "%s, the observations for %s are: Temperature: %s; Humidity %s; Dew Point: %s; Wind: %s; Pressure: %s; Current Conditions: %s" % (updated, city, temp, humidity, dewpoint, wind, pressure, conditions)

# Return regular string, let PHP handle the JSON-style output
#json = """{
#  "text": "%s"
#}""" % output
print output
