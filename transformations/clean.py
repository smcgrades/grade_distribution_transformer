import pandas as pd
import csv


def csv(file_path):
    # New CSV file name
    updated_csv_file = file_path.split(".csv")[0] + "_cleaned.csv"

    # Read the CSV file into the Dataframe
    df = pd.read_csv(file_path)

    # Remove rows where the 'Department' column has the specified value
    df = df[df['Department'] != 'Fall 2021 Grade Distribution by Instructor']

    # Get the header as a list of column names
    header = df.columns.tolist()

    # Remove rows that are identical to the header
    df = df[~df.apply(lambda row: row.tolist() == header, axis=1)]

    # Save the updated DataFrame to a new CSV file
    df.to_csv(updated_csv_file, index=False)

    print(f"The first row has been removed. Output saved to '{updated_csv_file}'.")
