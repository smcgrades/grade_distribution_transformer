import pandas as pd

# Ask the user for the XLSX file path
xlsx_file = input("Enter the path to the XLSX file: ")

# Determine the CSV file name by removing the file extension and adding .csv
csv_file = xlsx_file.split(".xlsx")[0] + ".csv"

# Read the XLSX file into a DataFrame
df = pd.read_excel(xlsx_file)

# Save the DataFrame as a CSV file
df.to_csv(csv_file, index=False)

print(f"XLSX file '{xlsx_file}' converted to CSV file '{csv_file}' successfully.")
