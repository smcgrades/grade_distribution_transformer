import pandas as pd
import json


def lists(file_path):
    # New JSON file name
    completed_json_file = file_path.split("_cleaned.csv")[0] + ".json"
    courses_json_file = file_path.split("_cleaned.csv")[0] + "_courses.json"
    instructors_json_file = file_path.split("_cleaned.csv")[0] + "_instructors.json"

    # Read the CSV file into the Dataframe
    df = pd.read_csv(file_path)

    # Get the 'Course' column as a list
    course_list = df['Course'].values.tolist()
    unique_courses = pd.Series(course_list).drop_duplicates().tolist()
    # with open(courses_json_file, 'w') as json_file:
    #     json.dump(unique_courses, json_file)
    # print(f"{courses_json_file} has been created!")

    # Get the 'Instructor' column as a list
    instructor_list = df['Instructor'].values.tolist()
    unique_instructors = pd.Series(instructor_list).drop_duplicates().tolist()
    # with open(instructors_json_file, 'w') as json_file:
    #     json.dump(unique_instructor, json_file)
    # print(f"{instructors_json_file} has been created!")

    if len(unique_courses) == len(unique_instructors):
        print("Course and Instructor unique lists are the same")


