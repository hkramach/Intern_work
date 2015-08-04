import xml.dom.minidom
import urllib2

import trulia.stats
import trulia.location

import sys

#API key that I found after signing up and registering application
TRULIA_KEY = "9yh4y2jukgka5ubed56y9vew"

def getLocationData(city, state):

    url = 'http://api.trulia.com/webservices.php?library=LocationInfo&function=getCitiesInState'
    url += '&state=state&apikey=TRULIA_KEY'
    try:
        doc = xml.dom.minidom.parseString(urllib2.urlopen(url).read())
    except urllib2.HTTPError: 
        print "invalidkey error:", sys.exc_info()[0]
        return None
    code = doc.getElementsByTagName('code')[0].firstChild.data
    if code != '0': 
        return None
    if 1:
        # Get all cities in "state"
        cities = trulia.location.LocationInfo(TRULIA_KEY).get_cities_in_state(state)
        # Get all counties in "state"
        counties = trulia.location.LocationInfo(TRULIA_KEY).get_counties_in_state(state)
        # Get all neighborhoods in input city and state
        neighborhoods = trulia.location.LocationInfo(TRULIA_KEY).get_neighborhoods_in_city(city, state) 
        # Get all zip codes in "state"
        zip_codes = trulia.location.LocationInfo(TRULIA_KEY).get_zip_codes_in_state(state)
        #Get all states
        states = trulia.location.LocationInfo(TRULIA_KEY).get_states()
    else:
        return None
    return (zip_codes, nieghborhoods, counties, cities, states)

def getStats(city, state):

    # Get all traffic and listing stats for the input city in January 2014
    city_stats = trulia.stats.TruliaStats(TRULIA_KEY).get_city_stats(city=city, state=state, start_date="2014-01-01", end_date="2014-01-31")
    # Get all traffic and listing stats in January 2014
    county_stats = trulia.stats.TruliaStats(TRULIA_KEY).get_county_stats(city=city, state=state, start_date="2014-01-01", end_date="2014-01-31")
    # Get all traffic and listing stats for Venice, CA neighborhood in January 2014
    neighborhood_stats = trulia.stats.TruliaStats(TRULIA_KEY).get_neighborhood_stats(neighborhood_id=7183, start_date="2014-01-01", end_date="2014-01-31")
    # Get all traffic and listing stats for California in January 2014
    state_stats = trulia.stats.TruliaStats(TRULIA_KEY).get_state_stats(state=state, start_date="2014-01-01", end_date="2014-01-31")
    #Get zip code stats
    zip_stats = trulia.stats.TruliaStats(TRULIA_KEY).get_zip_code_stats(zip_code=”94087”, start_date=”2014-01-01”, end_date=”2014-01-31”)

    return(city_stats, county_stats, neighborhood_stats, state_stats, zip_stats)

if __name__ == "__main__":
  print(getLocationData("Sunnyvale", "CA"))
  print(getStats("Sunnyvale", "CA"))



