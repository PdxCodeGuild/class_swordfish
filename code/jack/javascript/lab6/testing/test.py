import json

with open('./City_Boundaries.geojson', 'r') as f:
    doc = f.read()
pdx_boundary = json.loads(doc)

def get_coordinates(city_name):
    for feature in pdx_boundary['features']:
        if feature["properties"]['CITYNAME'] == city_name:
            return feature['geometry']['coordinates']
print(len(get_coordinates('Portland')[0][0]))

