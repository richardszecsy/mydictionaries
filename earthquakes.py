'''
the eq_data file is a json file that contains detailed information about
earthquakes around the world for a period of a month.

NOTE: No hard-coding allowed except for keys for the dictionaries

1) print out the number of earthquakes

2) iterate through the dictionary and extract the location, magnitude, 
   longitude and latitude of the location and put it in a new
   dictionary, name it 'eq_dict'. We are only interested in earthquakes that have a 
   magnitude > 6. Print out the new dictionary.

3) using the eq_dict dictionary, print out the information as shown below (first three shown):

Location: Northern Mid-Atlantic Ridge
Magnitude: 6.2
Longitude: -36.0923
Latitude: 35.4364


Location: 166km SSE of Muara Siberut, Indonesia
Magnitude: 6.1
Longitude: 100.0208
Latitude: -2.8604


Location: 14km ENE of Puerto Madero, Mexico
Magnitude: 6.6
Longitude: -92.2981
Latitude: 14.7628

'''
import json
#1-----------------------------------------
infile = open('eq_data.json', 'r')
data = json.load(infile)

print('Number of earthquakes', data['metadata']['count'])
#2--------------------------------------------
newdict = {}
eq_dict = {'earthquakes':[]}
for row in range(len(data['features'])):
   if data['features'][row]['properties']['mag']>6:
      newdict['location'] = data['features'][row]['properties']['place']
      newdict['magnitude'] = data['features'][row]['properties']['mag']
      newdict['longitude'] = data['features'][row]['geometry']['coordinates'][0]
      newdict['latitude'] = data['features'][row]['geometry']['coordinates'][1]
      eq_dict['earthquakes'].append(newdict)
print()
print(eq_dict['earthquakes'])
#3------------------------------------------------
for features in data['features']:
   if features['properties']['mag']>6:
      print(f"Location: {features['properties']['place']}")
      print(f"Magnitude: {features['properties']['mag']}")
      print(f"Longitude: {features['geometry']['coordinates'][0]}")
      print(f"Latitude: {features['geometry']['coordinates'][1]}")
      print()
      print()
      print()

