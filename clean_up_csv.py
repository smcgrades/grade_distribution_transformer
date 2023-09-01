import pandas as pd

# Input CSV file path
original_csv_file = input("Enter the path to the CSV file: ")
updated_csv_file = original_csv_file.split(".xlsx")[0] + "_cleaned.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(original_csv_file)

# Remove empty rows (rows with all NaN values)
df = df.dropna(how="all")

# Fill empty cells in specified columns with the values from the cell above
columns_to_fill = ["Department", "Discipline", "Course"]
df[columns_to_fill] = df[columns_to_fill].fillna(method="ffill")

# Remove extra spaces between words in the "Course" column
df["Course"] = df["Course"].str.replace(r'\s+', ' ', regex=True)

# Replace values in the "Department" column
department_replacements = {
    "CSIS": "Computer Science and Information Systems (CSIS)",
    "Disabl Stu Ctr": "Disabled Student Center",
    "Education/ECE": "Education and Early Childhood",
    "ESL": "English as a Second Language (ESL)",
    "Modern Lang/Cul": "Modern Language and Cultures",
    "Philosophy/Soci": "Philosophy and Social Sciences",
    "Photo - Fashion": "Photography and Fashion",
    "Physical Sci": "Physical Sciences"
}

df["Department"] = df["Department"].replace(department_replacements)

# Fill empty cells in specified columns with 0 and convert to numeric
columns_to_convert_to_numeric = ["A", "B", "C", "D", "F", "P", "NP", "IX", "SP", "W", "EW", "TotalCount"]
df[columns_to_convert_to_numeric] = df[columns_to_convert_to_numeric].fillna(0).apply(pd.to_numeric, errors="coerce")

# Save the modified DataFrame to a new CSV file
df.to_csv(updated_csv_file, index=False)

print(f"CSV file '{original_csv_file}' created successfully with empty rows removed, cells filled, and Course column "
      f"cleaned.")