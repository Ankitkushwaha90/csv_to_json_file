import csv
import json

def csv_to_json(csv_file):
    # Read CSV file and convert it to a list of dictionaries
    with open(csv_file, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = list(csv_reader)

    # Print the data in JSON format
    json_data = json.dumps(data, indent=4)
    print(json_data)

# Replace 'input.csv' with the name of your CSV file
csv_to_json('datas.csv')