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
        print(f"Running transformation on: {file_path}")
        csv_file_path = convert.xlsx_to_csv(file_path)
        cleaned_csv_file_path = clean.csv(csv_file_path)
        create.lists(cleaned_csv_file_path)
        print(f"Finished transformation on: {file_path}\n")


def main():
    directory:str
    print(f"----------------------------\nWelcome to the Pipeline!\n----------------------------")
    print("This python script transforms .xlsx files into usable csv files.")
    print("Read about how to prepare the environment for this script to work as intended in the README.md.")
    # This will come in a later feature.
    # option = input("Would you like to provide your own folder or use the 'grades' folder provided?"
    #                " (Type 'Own' or 'Grades'): ")
    # if option == 'Own':
    #     directory = input("Please provide the path to your directory here: ")
    #     remove.all_other_files(directory)
    # elif option == 'Grades':
    #     directory = "grades"
    #     remove.all_other_files("grades")
    # else:
    #     print("Please type 'Own' or 'Grades' (case sensitive).")
    #     exit(0)
    directory = "grades"
    remove.all_other_files(directory)
    file_paths = collect_files(directory)
    print(f"\nWe found the following files in the {directory} folder: ")
    for file_path in file_paths:
        print(file_path)
    confirm = input("\nAre these the correct files? (Type 'Yes' or 'No'): ")
    if confirm == 'Yes':
        print("Perfect! Let's start the script...\n")
        run_transformations(file_paths)
    elif confirm == 'No':
        print("Go ahead and make the changes to your folder and rerun the program.")
        exit(0)


main()
