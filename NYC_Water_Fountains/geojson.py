import csv
import json

# Open the CSV file
with open('NYC_Water_Fountains.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # skip header row

    # Define a GeoJSON FeatureCollection to store the fountain locations
    features = {'type': 'FeatureCollection', 'features': []}

    # Loop through each row of the CSV file
    for row in csv_reader:
        # Extract the fountain location information
        lat = float(row[0])
        lon = float(row[1])
        name = row[2]

        # Create a GeoJSON feature for the fountain
        feature = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [lon, lat]
            },
            'properties': {
                'name': name
            }
        }

        # Add the feature to the FeatureCollection
        features['features'].append(feature)

# Write the GeoJSON to a file
with open('NYC_Water_Fountains.geojson', 'w') as outfile:
    json.dump(features, outfile)
