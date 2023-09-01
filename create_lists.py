import pandas as pd
import json


# Function to extract unique values from a column and update a set
def extract_and_update_unique_values(df, column_name, unique_set):
    unique_values = df[column_name].unique()
    unique_set.update(unique_values)


# Function to save a set to a JSON file
def save_set_to_json(unique_set, output_file_name):
    with open(output_file_name, 'w') as json_file:
        json.dump(list(unique_set), json_file)


# Initialize an empty set to store unique courses across all files
all_unique_courses = set()
all_unique_instructors = set()

while True:
    # Ask the user for the path to a CSV file or enter 'q' to quit
    csv_file_path = input("Enter the path to a CSV file (or 'q' to quit): ")

    if csv_file_path.lower() == 'q':
        break

    try:
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(csv_file_path)

        # Get unique courses and update the set
        extract_and_update_unique_values(df, "Course", all_unique_courses)
        extract_and_update_unique_values(df, "Instructor", all_unique_instructors)

        print(f"Unique courses and instructors from {csv_file_path} have been added.")


    except FileNotFoundError:
        print(f"File not found: {csv_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Save the set of all unique courses to a JSON file
save_set_to_json(all_unique_courses, "courses.json")
save_set_to_json(all_unique_instructors, "instructors.json")

print("All unique courses and instructors have been saved to 'courses.json' and 'instructors.json.'")
