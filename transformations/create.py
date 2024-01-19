import pandas as pd
import json

def create_class_lists(file_path):
    # Define the output file name
    output_file = file_path.replace("_cleaned.csv", ".json")

    # Load the data from the CSV file
    data_frame = pd.read_csv(file_path)
    records = data_frame.to_dict(orient='records')

    # Extract unique instructor-course pairs
    unique_pairs = set((data["Instructor"], data["Course"]) for data in records if data["Instructor"] and data["Course"])

    # Prepare the final data
    final_data = []

    for instructor, course in unique_pairs:
        # Filter records for the current instructor-course pair
        matching_records = [data for data in records if data["Instructor"] == instructor and data["Course"] == course]

        # Initialize the combined data
        combined_data = {
            "total_a": 0.0,
            "total_b": 0.0,
            "total_c": 0.0,
            "total_d": 0.0,
            "total_f": 0.0,
            "total_p": 0.0,
            "total_np": 0.0,
            "total_ix": 0.0,
            "total_rd": 0.0,
            "total_sp": 0.0,
            "total_w": 0.0,
            "total_ew": 0.0,
            "total_students": 0.0
        }

        # Combine the data for the current instructor-course pair
        for record in matching_records:
            for key in combined_data.keys():
                combined_data[key] += record.get(key.split("_")[1].upper(), 0.0)

        # Add the common data
        combined_data.update({
            "department": matching_records[0]["Department"],
            "subject": matching_records[0]["Subject"],
            "course": course,
            "instructor": instructor
        })

        # Add the combined data to the final data
        final_data.append(combined_data)

    # Save the final data to the output file
    with open(output_file, 'w') as json_file:
        json.dump(final_data, json_file, indent=4)

    print(f"Formatted JSON file saved to {output_file}")