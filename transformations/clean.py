import pandas as pd

def csv(file_path):
    # New CSV file name
    updated_csv_file = file_path.split(".csv")[0] + "_cleaned.csv"

    # Read the CSV file into the Dataframe
    df = pd.read_csv(file_path)

    text_to_remove = "Fall 2021 Grade Distribution by Instructor"

    filtered_df = df[~df.apply(lambda row: text_to_remove in row.to_string(), axis=1)]
    filtered_df.to_csv(updated_csv_file, index=False)
    print(f"Rows containing '{text_to_remove} has been removed.")
