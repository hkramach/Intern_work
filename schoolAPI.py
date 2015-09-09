import xml.dom.minidom
import urllib2
import urllib

API_KEY = 'ieyela0cc4agimgtwkithqxx'
f = { 'key' : API_KEY}

def school_census(state_of_choice, school_ID):
  #param = urllib.urlencode(f)
  baseurl = 'http://api.greatschools.org/school/census/'
  url = baseurl + state_of_choice + '/' + school_ID + '?key=' + API_KEY
  print url
  req = urllib2.Request(url)
  response = urllib2.urlopen(req)
  doc = xml.dom.minidom.parseString(response.read())
  address = doc.getElementsByTagName("address")[0]
  latitude = doc.getElementsByTagName("latitude")[0]
  longitude = doc.getElementsByTagName("longitude")[0]
  phone = doc.getElementsByTagName("phone")[0]
  school_type = doc.getElementsByTagName("type")[0]
  district = doc.getElementsByTagName("district")[0]
  enrollment = doc.getElementsByTagName("enrollment")[0]
  freeAndReducedPriceLunch = doc.getElementsByTagName("freeAndReducedPriceLunch")[0]
  #studentTeacherRatio = doc.getElementsByTagName("studentTeacherRatio")[0]
  print (address.toxml())
  print (latitude.toxml())
  print (longitude.toxml())
  print (phone.toxml())
  print (school_type.toxml())
  print (district.toxml())
  print (enrollment.toxml())
  print (freeAndReducedPriceLunch.toxml())
  #print (studentTeacherRatio.toxml())
  ethnicities = doc.getElementsByTagName("ethnicities")
  for ethnicity in ethnicities:
    for i in range (0, 5):
      name = ethnicity.getElementsByTagName("name")[i]
      value = ethnicity.getElementsByTagName("value")[i]
      year = ethnicity.getElementsByTagName("year")[i]
      print (name.toxml())
      print (value.toxml())
      print (year.toxml())
      print ("-------------------------------------------")
  return doc.getElementsByTagName("schoolName")[0]

def school_test_scores(state_of_choice, school_ID):
  baseurl = 'http://api.greatschools.org/school/tests/'
  url = baseurl + state_of_choice + '/' + school_ID + '?key=' + API_KEY
  print url
  req = urllib2.Request(url)
  response = urllib2.urlopen(req)
  doc = xml.dom.minidom.parseString(response.read())
  rank = doc.getElementsByTagName("rank")
  for ranks in rank:
    name = ranks.getElementsByTagName("name")[0]
    scale = ranks.getElementsByTagName("scale")[0]
    year = ranks.getElementsByTagName("year")[0]
    description = ranks.getElementsByTagName("description")[0]
    score = ranks.getElementsByTagName("score")[0]
    print (name.toxml())
    print (scale.toxml())
    print (year.toxml())
    print (description.toxml())
    print (score.toxml())
  test = doc.getElementsByTagName("test")
  for tests in test:
    name = tests.getElementsByTagName("name")[0]
    iD = tests.getElementsByTagName("id")[0]
    description = tests.getElementsByTagName("description")[0]
    abbreviation = tests.getElementsByTagName("abbreviation")[0]
    scale = tests.getElementsByTagName("scale")[0]
    levelCode = tests.getElementsByTagName("levelCode")[0]
    testResult = tests.getElementsByTagName("testResult")
    print (name.toxml())
    print (iD.toxml())
    print (description.toxml())
    print (abbreviation.toxml())
    print (scale.toxml())
    print (levelCode.toxml())
    for results in testResult:
      for i in range(0, 1):
        gradeName = results.getElementsByTagName("gradeName")[0]
        score = results.getElementsByTagName("score")[0]
        subjectName = results.getElementsByTagName("subjectName")[0]
        testId = results.getElementsByTagName("testId")[0]
        year = results.getElementsByTagName("year")[0]
        print (gradeName.toxml())
        print (score.toxml())
        print (subjectName.toxml())
        print (testId.toxml())
        print (year.toxml())
        print ("------------")
  return doc.getElementsByTagName("schoolName")[0]

def nearby_schools(state_of_choice, city_of_choice, add, zc, type_of_school, level, dist, numSchools):
  baseurl0 = 'http://api.greatschools.org/schools/nearby'
  baseurl1 = baseurl0+'?key='+API_KEY+'&address='+add+'&city='+city_of_choice+'&state='+state_of_choice
  url = baseurl1+'&zip='+zc+'&schoolType='+type_of_school+'&levelCode='+level+'&radius='+dist+'&limit='+numSchools
  print url
  req = urllib2.Request(url)
  response = urllib2.urlopen(req)
  doc = xml.dom.minidom.parseString(response.read())
  school = doc.getElementsByTagName("school")
  for schools in school:
    gsId = schools.getElementsByTagName("gsId")[0]
    name = schools.getElementsByTagName("name")[0]
    type_of_school = schools.getElementsByTagName("type")[0]
    gradeRange = schools.getElementsByTagName("gradeRange")[0]
    enrollment = schools.getElementsByTagName("enrollment")[0]
    city = schools.getElementsByTagName("city")[0]
    state = schools.getElementsByTagName("state")[0]
    address = schools.getElementsByTagName("address")[0]
    phone = schools.getElementsByTagName("phone")[0]
    ncesId = schools.getElementsByTagName("ncesId")[0]
    lat = schools.getElementsByTagName("lat")[0]
    lon = schools.getElementsByTagName("lon")[0]
    overviewLink = schools.getElementsByTagName("overviewLink")[0]
    ratingsLink = schools.getElementsByTagName("ratingsLink")[0]
    reviewsLink = schools.getElementsByTagName("reviewsLink")[0]
    print (gsId.toxml())
    print (name.toxml())
    print (type_of_school.toxml())
    print (gradeRange.toxml())
    print (enrollment.toxml())
    print (city.toxml())
    print (state.toxml())
    print (address.toxml())
    print (phone.toxml())
    print (ncesId.toxml())
    print (lat.toxml())
    print (lon.toxml())
    print (overviewLink.toxml())
    print (ratingsLink.toxml())
    print (reviewsLink.toxml())
    print ("---------------")
  return doc.getElementsByTagName("schools")

def city_overview(state_of_choice, city_of_choice):
  baseurl = 'http://api.greatschools.org/cities/'
  url = baseurl + state_of_choice + '/' + city_of_choice + '?key=' + API_KEY
  print url
  req = urllib2.Request(url)
  response = urllib2.urlopen(req)
  doc = xml.dom.minidom.parseString(response.read())
  city = doc.getElementsByTagName("city")
  for cities in city:
    name = cities.getElementsByTagName("name")[0]
    rating = cities.getElementsByTagName("rating")[0]
    totalSchools = cities.getElementsByTagName("totalSchools")[0]
    elementarySchools = cities.getElementsByTagName("elementarySchools")[0]
    middleSchools = cities.getElementsByTagName("middleSchools")[0]
    highSchools = cities.getElementsByTagName("highSchools")[0]
    publicSchools = cities.getElementsByTagName("publicSchools")[0]
    charterSchools = cities.getElementsByTagName("charterSchools")[0]
    privateSchools = cities.getElementsByTagName("privateSchools")[0]
    print (name.toxml())
    print (rating.toxml())
    print (totalSchools.toxml())
    print (elementarySchools.toxml())
    print (middleSchools.toxml())
    print (highSchools.toxml())
    print (publicSchools.toxml())
    print (charterSchools.toxml())
    print (privateSchools.toxml())
    print ("----------------")
  return city

def nearby_cities(state_of_choice, city_of_choice, distance, sorting):
  baseurl = 'http://api.greatschools.org/cities/nearby/'
  url = baseurl+state_of_choice+'/'+city_of_choice+'?key='+API_KEY+'&radius='+distance+'&sort='+sorting
  print url
  req = urllib2.Request(url)
  response = urllib2.urlopen(req)
  doc = xml.dom.minidom.parseString(response.read())
  city = doc.getElementsByTagName("city")
  for cities in city:
    for i in range(0, 1):
      name = cities.getElementsByTagName("name")[0]
      rating = cities.getElementsByTagName("rating")[0]
      totalSchools = cities.getElementsByTagName("totalSchools")[0]
      elementarySchools = cities.getElementsByTagName("elementarySchools")[0]
      middleSchools = cities.getElementsByTagName("middleSchools")[0]
      highSchools = cities.getElementsByTagName("highSchools")[0]
      publicSchools = cities.getElementsByTagName("publicSchools")[0]
      charterSchools = cities.getElementsByTagName("charterSchools")[0]
      privateSchools = cities.getElementsByTagName("privateSchools")[0]
      print (name.toxml())
      print (rating.toxml())
      print (totalSchools.toxml())
      print (elementarySchools.toxml())
      print (middleSchools.toxml())
      print (highSchools.toxml())
      print (publicSchools.toxml())
      print (charterSchools.toxml())
      print (privateSchools.toxml())
      print ("----------------")
  return doc.getElementsByTagName("cities")

def browse_districts(state_of_choice, city_of_choice):
  baseurl = 'http://api.greatschools.org/districts/'
  url = baseurl + state_of_choice + '/' + city_of_choice + '?key=' + API_KEY
  print url
  req = urllib2.Request(url)
  response = urllib2.urlopen(req)
  doc = xml.dom.minidom.parseString(response.read())
  district = doc.getElementsByTagName("district")
  for dist in district:
    for i in range(0, 1):
      name = dist.getElementsByTagName("name")[0]
      ncesCode = dist.getElementsByTagName("ncesCode")[0]
      districtRating = dist.getElementsByTagName("districtRating")[0]
      address = dist.getElementsByTagName("address")[0]
      phone = dist.getElementsByTagName("phone")[0]
      fax = dist.getElementsByTagName("fax")[0]
      website = dist.getElementsByTagName("website")[0]
      gradeRange = dist.getElementsByTagName("gradeRange")[0]
      totalSchools = dist.getElementsByTagName("totalSchools")[0]
      elementarySchools = dist.getElementsByTagName("elementarySchools")[0]
      middleSchools = dist.getElementsByTagName("middleSchools")[0]
      highSchools = dist.getElementsByTagName("highSchools")[0]
      publicSchools = dist.getElementsByTagName("publicSchools")[0]
      charterSchools = dist.getElementsByTagName("charterSchools")[0]
      print (name.toxml())
      print (ncesCode.toxml())
      print (districtRating.toxml())
      print (address.toxml())
      print (phone.toxml())
      print (fax.toxml())
      print (website.toxml())
      print (gradeRange.toxml())
      print (totalSchools.toxml())
      print (elementarySchools.toxml())
      print (middleSchools.toxml())
      print (highSchools.toxml())
      print (publicSchools.toxml())
      print (charterSchools.toxml())
  return doc.getElementsByTagName("districts")

if __name__ == "__main__":
  choice = raw_input ("census, nearby schools, test scores, nearby cities, city schools, or districts?")
  if choice == "census":
    state = raw_input("Give a state in abbreviation")
    iD = raw_input("Give the school ID")
    print(school_census(state, iD).toxml())
  if choice == "test scores":
    state = raw_input("Give state in abbreviation")
    iD = raw_input("Give school ID")
    print (school_test_scores(state, iD).toxml())
  if choice == "nearby schools":
    print (nearby_schools('CA', 'San+Francisco', '160+Spear+St', '94105', 'public-charter', 'high-schools', '5', '1').toxml())
  if choice == "nearby cities":
    print (nearby_cities('CA', 'Bakersfield', '16', 'rating').toxml())
  if choice == "city schools":
    print (city_overview('TX', 'Dallas').toxml())
  if choice == "districts":
    print (browse_districts('CA', 'San-Francisco'))


