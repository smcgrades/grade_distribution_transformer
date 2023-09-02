import pandas as pd

def clean_up_csv(file_path):
    # Input CSV file path
    updated_csv_file = file_path.split(".csv")[0] + "_cleaned.csv"

    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Remove empty rows (rows with all NaN values)
    df = df.dropna(how="all")

    # Fill empty cells in specified columns with the values from the cell above
    columns_to_fill = ["Department", "Discipline", "Course"]
    df[columns_to_fill] = df[columns_to_fill].fillna(method="ffill")

    # Remove extra spaces between words in the "Course" column
    df["Course"] = df["Course"].str.replace(r'\s+', ' ', regex=True)

    # Fill empty cells in specified columns with 0 and convert to numeric
    columns_to_convert_to_numeric = ["A", "B", "C", "D", "F", "P", "NP", "IX", "SP", "W", "EW", "TotalCount"]
    df[columns_to_convert_to_numeric] = df[columns_to_convert_to_numeric].fillna(0).apply(pd.to_numeric, errors="coerce")

    # Save the modified DataFrame to a new CSV file
    df.to_csv(updated_csv_file, index=False)

    print(f"CSV file '{file_path}' created successfully with empty rows removed, cells filled, and Course column "
          f"cleaned.")
    return updated_csv_file