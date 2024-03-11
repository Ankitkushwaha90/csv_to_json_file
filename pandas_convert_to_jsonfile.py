import csv
import json

def csv_to_json(csv_file, json_file):
    # Read CSV file and convert it to a list of dictionaries
    with open(csv_file, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = list(csv_reader)

    # Write the list of dictionaries to a JSON file
    with open(json_file, 'w') as json_file:
        json.dump(data, json_file, indent=4)

# Example usage:
csv_to_json('datas.csv', 'datas.json')