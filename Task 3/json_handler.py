import json

def load_json_data(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            print("JSON Data:", data)

    except FileNotFoundError:
        print("Error: JSON file not found")

    except json.JSONDecodeError:
        print("Error: Invalid JSON format")