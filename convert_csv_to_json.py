import pandas as pd


def convert_csv_to_json(file_path):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Convert the DataFrame to a JSON object and save it to a JSON file
    new_json_file = file_path.split(".csv")[0] + ".json"
    df.to_json(new_json_file, orient='records', lines=True)

    df = pd.read_csv(file_path)

    # Convert the DataFrame to a list of dictionaries (each row is an object)
    data_list = df.to_dict(orient='records')

    # Write the list of dictionaries to a JSON file
    with open(new_json_file, 'w') as json_file:
        import json
        json.dump(data_list, json_file, indent=4)

    print(f'CSV file "{file_path}" has been converted to JSON file "{new_json_file}"')
    return new_json_file

