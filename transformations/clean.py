import pandas as pd

rowsToRemove = ['Fall 2020 Grade Distribution by Instructor', 'Fall 2021 Grade Distribution by Instructor',
                'Spring 2021 Grade Distribution by Instructor', 'Spring 2022 Grade Distribution by Instructor']
columnsToFill = ['Department', 'Discipline', 'Course']
columnsToConvert = ["A", "B", "C", "D", "F", "P", "NP", "IX", "RD", "SP", "W", "EW", "Total"]
departmentReplacements = {
    "Communication": "Communication and Media Studies",
    "Communicatio": "Communication and Media Studies",
    "CSIS": "Computer Science and Information Systems (CSIS)",
    "Computer Scie": "Computer Science and Information Systems (CSIS)",
    "Design Technolo": "Design Technology",
    "Design Techno": "Design Technology",
    "Disabl Stu Ctr": "Disabled Student Center",
    "Disabled Stud": "Disabled Student Center",
    "Earth Science": "Earth Sciences",
    "Education/ECE": "Education and Early Childhood",
    "ESL": "English as a Second Language (ESL)",
    "Health Science": 'Health Sciences',
    "Kinesiology and": "Kinesiology and Athletics",
    "Kinesiology an": "Kinesiology and Athletics",
    "Athletics": "Kinesiology and Athletics",
    "Kinesiology": "Kinesiology and Athletics",
    "Life Science": "Life Sciences",
    "Math": "Mathematics",
    "Modern Lang/Cu": "Modern Languages and Culture",
    "Modern Lang/Cul": "Modern Languages and Culture",
    "Modern Lang/C": "Modern Languages and Culture",
    "Modern Langu": "Modern Languages and Culture",
    "Noncredit Educa": "Noncredit Education",
    "Noncredit": "Noncredit Education",
    "Noncredit Edu": "Noncredit Education",
    "Philosophy/Soci": "Philosophy and Social Sciences",
    "Philosophy/So": "Philosophy and Social Sciences",
    "Philosophy an": "Philosophy and Social Sciences",
    "Photo - Fashion": "Photography and Fashion",
    "Photo - Fashio": "Photography and Fashion",
    "Photography a": "Photography and Fashion",
    "Physical Sci": "Physical Sciences",
    "Physical Scien": "Physical Sciences",
}


def csv(file_path):
    # New CSV file name
    updated_csv_file = file_path.split(".csv")[0] + "_cleaned.csv"

    # Read the CSV file into the Dataframe
    df = pd.read_csv(file_path)

    # Get the header as a list of column names
    header = df.columns.tolist()

    # Remove rows that are identical to the header
    df = df[~df.apply(lambda row: row.tolist() == header, axis=1)]

    # Check if the first header column is not named 'Department' and rename it
    if df.columns[0] != 'Department':
        df.columns.values[0] = 'Department'

    # Find IX in the header
    if 'IX' in header:
        ix_index = header.index("IX")

        # Check if 'RD' is after 'IX'
        if 'RD' not in df.columns[ix_index + 1:]:
            # Add 'RD' after 'IX' in the DataFrame
            df.insert(ix_index + 1, 'RD', None)

    if 'RD' in header:
        ix_index = header.index("RD")

        # Check if 'SP' is after 'RD'
        if 'SP' not in df.columns[ix_index + 1:]:
            # Add 'SP' after 'RD' in the DataFrame
            df.insert(ix_index + 1, 'SP', None)

    # Check if the last header column is not named 'Total' and rename it
    if df.columns[-1] != 'Total':
        df.columns.values[-1] = 'Total'

    df = df[~df['Department'].isin(rowsToRemove)]

    # Replace all incorrect values in column 'Department'
    df['Department'] = df['Department'].replace(departmentReplacements)

    # Fill empty cells in certain columns with values from the cell above
    df[columnsToFill] = df[columnsToFill].ffill()

    # Remove extra spaces between words in the "Course" column
    df["Course"] = df["Course"].str.replace(r'\s+', ' ', regex=True)

    # Fill empty cells in certain columns with 0 and convert to numeric
    df[columnsToConvert] = df[columnsToConvert].fillna(0).astype(float)

    # Save the updated DataFrame to a new CSV file
    df.to_csv(updated_csv_file, index=False)

    print(f"{file_path} has been cleaned to {updated_csv_file}!")
    return updated_csv_file
