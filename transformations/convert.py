import pandas as pd
import os


def xlsx_to_csv(file_path):
    print(f"Converting {file_path} into a csv file...")
    file_without_extension = file_path.split("grades/")[1].split(".xlsx")[0]
    path = "grades/" + file_without_extension
    os.mkdir(path)
    new_csv_file = "grades/" + file_without_extension + "/" + file_without_extension + ".csv"
    print(new_csv_file)
    df = pd.read_excel(file_path)
    df.to_csv(new_csv_file, index=False, header=False)
    print(f"{file_path} converted to {new_csv_file}!")
    return new_csv_file

# def csv_to_json(file_path):
#     print(f"Converting {file_path} into a json file...")
#     new_json_file = file_path.split(".csv")[0] + ".json"
#     df = pd.read_csv(file_path)
#     data_list = df.to_dict(orient='records')
#     with open(new_json_file, 'w') as json_file:
#         import json
#         json.dump(data_list, json_file, indent=4)
#     print(f"{file_path} has been converted to {new_json_file}!")
#     return new_json_file
