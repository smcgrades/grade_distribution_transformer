import pandas as pd
import os


def xlsx_to_csv(file_path):
    file_without_extension = file_path.split("grades/")[1].split(".xlsx")[0]
    path = "grades/" + file_without_extension
    os.mkdir(path)
    new_csv_file = "grades/" + file_without_extension + "/" + file_without_extension + ".csv"
    df = pd.read_excel(file_path)
    df.to_csv(new_csv_file, index=False, header=False)
    print(f"{file_path} converted to {new_csv_file}!")
    return new_csv_file

