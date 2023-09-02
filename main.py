from convert_xlsx_to_csv import convert_xlsx_to_csv
from clean_up_csv import clean_up_csv
from convert_csv_to_json import convert_csv_to_json


def main():
    print("Hello there! This script helps automate the process of cleaning up and preparing a xlsx file.")
    file_path = input("Provide the path of the file: ")
    csv_file = convert_xlsx_to_csv(file_path)
    approval = input("Before we move forward, go ahead and access the csv file created. Then make "
                     "modifications.\nOnce you are done type Done to continue: ")
    cleaned_csv_file = clean_up_csv(csv_file)
    json_file = convert_csv_to_json(cleaned_csv_file)


main()
