import os
from transformations import convert, clean, create, remove


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
        cleaned_csv_file_path = clean.csv(csv_file_path)
        create.lists(cleaned_csv_file_path)
        print(f"Finished script on: {file_path}\n")

def main():
    remove.all_other_files("grades")
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
    print("Perfect! Let's start the script...\n")
    run_transformations(file_paths)


main()
