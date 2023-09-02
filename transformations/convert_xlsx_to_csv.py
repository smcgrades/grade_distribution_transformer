import pandas as pd


def convert_xlsx_to_csv(file_path):
    # Determine the CSV file name by removing the file extension and adding .csv
    new_file_name = file_path.split(".xlsx")[0] + ".csv"

    # Read the XLSX file into a DataFrame
    df = pd.read_excel(file_path)

    # Save the DataFrame as a CSV file
    df.to_csv(new_file_name, index=False)

    print(f"XLSX file '{file_path}' converted to CSV file '{new_file_name}' successfully.")
    return new_file_name
