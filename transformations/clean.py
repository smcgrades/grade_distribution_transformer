import pandas as pd
from fuzzywuzzy import process

def find_best_match(word, correct_departments):
    # Use process to find the best match with a similarity score
    matches = process.extractOne(word, correct_departments)

    # If a match is found and the similarity score is above a certain threshold (adjust as needed)
    if matches and matches[1] > 80:
        print(f"Found match for {word}: {matches[0]}")
        return matches[0]
    else:
        print(f"No match found for {word}")
        # If no matches are found or the similarity score is too low, handle it accordingly
        return None

def clean_csv(file_path):

    updated_csv_file = file_path.split(".csv")[0] + "_cleaned.csv"

    correct_Department_columns = ['Art', 'Athletics and Kinesiology', 'Business', 'Communication and Media Studies', 'Computer Science and Information Systems (CSIS)', 'Cosmetology', 'Counseling', 'Dance', 'Design Technology', 'Disabled Student Center', 'Earth Science', 'Education and Early Childhood', 'English', 'ESL', 'Health Science', 'History', 'Library', 'Life Science', 'Mathematics', 'Modern Languages and Culture', 'Music', 'Noncredit Education', 'Philosophy and Social Science', 'Photography and Fashion', 'Physical Science', 'Psychology', 'Student Life', 'Theatre Arts']

    # CSV in DataFrame
    df = pd.read_csv(file_path)

    print(df.iloc[0,0])

    # # Rename department columns to their correct names
    # for index, row in df.iterrows():
    #     if pd.notnull(row['Department']):
    #         correct_Department = find_best_match(row['Department'], correct_Department_columns)
    #         df.at[index, 'Department'] = correct_Department

    df.to_csv(updated_csv_file, index=False)