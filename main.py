import os
import glob
from transformations import convert, clean


def remove_ds_store_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == '.DS_Store':
                file_path = os.path.join(root, file)
                os.remove(file_path)
                print(f"Removed: {file_path}")


def remove_all_other_files(directory):
    all_files = os.listdir(directory)

    # Use glob to filter for .xlsx files
    xlsx_files = glob.glob(os.path.join(directory, '*.xlsx'))

    # Iterate through all files and remove those that are not .xlsx files
    for file in all_files:
        file_path = os.path.join(directory, file)

        # Check if the file is not an .xlsx file
        if file_path not in xlsx_files:
            try:
                os.remove(file_path)
                print(f"Removed: {file_path}")
            except Exception as e:
                print(f"Error removing {file_path}: {str(e)}")


def collect_files(folder_path):
    file_paths = []

    if os.path.exists(folder_path):
        for root, _, files in os.walk(folder_path):
            for file_name in files:
                file_paths.append(os.path.join(root, file_name))
    else:
        print(f"The folder '{folder_path}' does not exist.")

    return file_paths


def run_transformations(file_paths):
    for file_path in file_paths:
        print(f"Running script on: {file_path}")
        csv_file_path = convert.xlsx_to_csv(file_path)
        clean.csv(csv_file_path)


def main():
    remove_ds_store_files("grades")
    remove_all_other_files("grades")
    print(f"----------------------------\nWelcome to the Pipeline!\n----------------------------")
    print("This python script transforms .xlsx files into usable csv files.")
    print("Read about how to prepare the environment for this script to work as intended in the README.md.")
    file_paths = collect_files("grades")
    print("\nRunning script....")
    print("We found the following files in the 'grades' folder: ")
    for file_path in file_paths:
        print(file_path)
    confirm = input("\nAre these the correct files? (Type 'Yes' or 'No'): ")
    if confirm == 'No':
        print("Alright then, go ahead and make the changes the comeback and rerun the program.")
        exit(0)
    print("Perfect! Let's start the script...")
    run_transformations(file_paths)


main()
