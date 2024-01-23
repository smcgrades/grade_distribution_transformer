import pandas as pd
from fuzzywuzzy import process

headers_to_remove = ['fall_2020/fall_2020', 'fall_2021/fall_2021', 'fall_2022/fall_2022', 'spring_2021/spring_2021', 'spring_2022/spring_2022', 'spring_2023/spring_2023']
rowsToRemove = ['Fall 2020 Grade Distribution by Instructor', 'Fall 2021 Grade Distribution by Instructor', 'Fall 2022 Grade Distribution by Instructor', 'Spring 2021 Grade Distribution by Instructor', 'Spring 2022 Grade Distribution by Instructor', 'Spring 2023 Grade Distribution by Instructor']
correct_Department_columns = ['Art', 'Athletics and Kinesiology', 'Business', 'Communication and Media Studies', 'Computer Science and Information Systems (CSIS)', 'Cosmetology', 'Counseling', 'Dance', 'Design Technology', 'Disabled Student Center', 'Earth Science', 'Education and Early Childhood', 'English', 'ESL', 'Health Science', 'History', 'Library', 'Life Science', 'Mathematics', 'Modern Languages and Culture', 'Music', 'Noncredit Education', 'Philosophy and Social Science', 'Photography and Fashion', 'Physical Science', 'Psychology', 'Student Life', 'Theatre Arts']
columnsToFill = ['Department', 'Subject', 'Course']



def find_best_match(word, correct_departments):
    # Use process to find the best match with a similarity score
    matches = process.extractOne(word, correct_departments)

    # If a match is found and the similarity score is above a certain threshold (adjust as needed)
    if matches and matches[1] > 80:
        # print(f'Found match for {word}: {matches[0]}')
        return matches[0]
    else:
        # print(f'No match found for {word}')
        # If no matches are found or the similarity score is too low, handle it accordingly
        return None

def clean_csv(file_path):

    updated_csv_file = file_path.split('.csv')[0] + '_cleaned.csv'

    # CSV in DataFrame
    df = pd.read_csv(file_path)

    # print(f'The incoming file path is: {file_path}\n')
    file_name_to_check = file_path.split('grades/')[1].split('.csv')[0]
    if(file_name_to_check in headers_to_remove):
        # Get the header as a list of column names
        header = df.columns.tolist()

        # Remove rows that are identical to the header
        df = df[~df.apply(lambda row: row.tolist() == header, axis=1)]

    
    # If first column is not named 'Department', rename it to 'Department'
    if df.columns[0] != 'Department':
        df.columns.values[0] = 'Department'
    
    # If second column is not named 'Subject', rename it to 'Subject'
    if df.columns[1] != 'Subject':
        df.columns.values[1] = 'Subject'
    
    if df.columns[2] != 'Course':
        df.columns.values[1] = 'Course'

    # If last column is not named 'Total', rename it to 'Total'
    if df.columns[-1] != 'Total':
        df.columns.values[-1] = 'Total'
    
    # Check 'Department' column for any cell that has any value in rowsToRemove and remove that row
    df = df[~df['Department'].isin(rowsToRemove)]

    # Remove extra spaces between words in the 'Course' column
    df['Course'] = df['Course'].str.replace(r'\s+', ' ', regex=True)

    # Check 'Department', 'Subject', 'Course', and 'Section' columns for any cell that has 'Total' in it and remove that row 
    df = df[~df['Department'].str.contains('Total', na=False)]
    df = df[~df['Subject'].str.contains('Total', na=False)]
    df = df[~df['Course'].str.contains('Total', na=False)]
    # Check if the header contains a cell named 'Section'
    if 'Section' in df.columns:
        # Check if 'Section' column is a number, if not remove that cell
        df = df[pd.to_numeric(df['Section'], errors='coerce').notnull()]

    # Rename department columns to their correct names
    for index, row in df.iterrows():
        if pd.notnull(row['Department']):
            correct_Department = find_best_match(row['Department'], correct_Department_columns)
            df.at[index, 'Department'] = correct_Department
    
    # Fill empty cells in certain columns with values from the cell above
    df[columnsToFill] = df[columnsToFill].ffill()

    # Any empty cell set to 0.0
    df = df.fillna(0.0)

    df.to_csv(updated_csv_file, index=False)

    return updated_csv_file