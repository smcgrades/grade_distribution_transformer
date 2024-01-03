import os
import pandas as pd
no_header_files = ['fall_2016', 'fall_2017', 'fall_2018', 'spring_2017', 'spring_2018', 'spring-2019']

def convert_xlsx_to_csv(file_path):
    file_without_extension = file_path.split("grades/")[1].split(".xlsx")[0]
    print(file_without_extension)
    path = "grades/" + file_without_extension
    os.mkdir(path)
    new_csv_file = "grades/" + file_without_extension + "/" + file_without_extension + ".csv"
    df = pd.read_excel(file_path)
    df.to_csv(new_csv_file, index=False, header=True)
    print(f"{file_path} converted to {new_csv_file}!\n")
    return new_csv_file

def collect_files(folder_path):
    file_paths = []

    if os.path.exists(folder_path):
        for root, _, files in os.walk(folder_path):
            for file_name in files:
                file_paths.append(os.path.join(root, file_name))
    else:
        print(f"The folder '{folder_path}' does not exist.")

    return file_paths

def delete_all_other_files(directory):
    for root, dirs, files in os.walk(directory, topdown=False):
        for file in files:
            if not file.endswith('.xlsx'):
                file_path = os.path.join(root, file)
                os.remove(file_path)

        for dir in dirs:
            dir_path = os.path.join(root, dir)
            os.rmdir(dir_path)
    print(f"{directory} folder has been cleaned.\n")