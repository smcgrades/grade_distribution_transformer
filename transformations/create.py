import pandas as pd
import json

def create_class_lists(file_path):
    # Define the output file name
    output_file = file_path.replace("_cleaned.csv", ".json")

    # Load the data from the CSV file
    df = pd.read_csv(file_path)
    records = df.to_dict(orient='records')

    # Extract unique instructor-course pairs
    unique_pairs = set((data["Instructor"], data["Course"]) for data in records if data["Instructor"] and data["Course"])

    # Prepare the final data
    classes = []

    for instructor, course in unique_pairs:
        # Filter records for the current instructor-course pair
        matching_records = [data for data in records if data["Instructor"] == instructor and data["Course"] == course]

        # Initialize the combined data
        individual_class = {
            "A": 0.0,
            "B": 0.0,
            "C": 0.0,
            "D": 0.0,
            "F": 0.0,
            "P": 0.0,
            "NP": 0.0,
            "IX": 0.0,
            "RD": 0.0,
            "SP": 0.0,
            "W": 0.0,
            "EW": 0.0,
            "Total": 0.0
        }

        # Combine the data for the current instructor-course pair
        for record in matching_records:
            for key in individual_class.keys():
                individual_class[key] += record.get(key, 0.0)

        individual_class.update({
            "Department": matching_records[0]["Department"],
            "Subject": matching_records[0]["Subject"],
            "Course": course,
            "Instructor": instructor
        })

        # Add the combined data to the final data
        classes.append(individual_class)

    # Save the final data to the output file
    with open(output_file, 'w') as json_file:
        json.dump(classes, json_file, indent=4)

    print(f"Formatted JSON file saved to {output_file}")