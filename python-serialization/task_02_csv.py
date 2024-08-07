import csv
import json
""" gain experience in reading data """


def convert_csv_to_json(csv_filename):
    """
    Convert CSV data to JSON format and write it to data.json.

    Parameters:
    csv_filename (str): The filename of the input CSV file.

    Returns:
    bool: True if the conversion was successful, False otherwise.
    """
    try:
        # Open the CSV file and read the data
        with open(csv_filename, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            # Convert rows into a list of dictionaries
            data = [row for row in csv_reader]

        # Serialize the list of dictionaries to JSON format
        with open('data.json', mode='w') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        print(f"File {csv_filename} not found.")
        return False

    except Exception as e:
        print(f"An error occurred: {e}")
        return False
