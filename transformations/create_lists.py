import json

# Load the JSON file
input_file = '/Users/asarelcastellanos/Desktop/smc_grades/fall_2021_cleaned.json'

with open(input_file, 'r') as file:
    data = json.load(file)

# Create a set to store unique instructor and course names
unique_names = set()

# Iterate through the data and extract instructor and course names
for entry in data:
    instructor = entry.get("Instructor")
    course = entry.get("Course")

    if instructor and course:
        unique_names.add((instructor, course))

# Convert the set of unique names into an array of objects
unique_names_array = [{"Instructor": instructor, "Course": course} for instructor, course in unique_names]

grouped_data = []

# Iterate through unique_names_array and find matching objects in data
for unique_name in unique_names_array:
    instructor = unique_name.get("Instructor")
    course = unique_name.get("Course")

    matching_objects = [entry for entry in data if
                        entry.get("Instructor") == instructor and entry.get("Course") == course]

    grouped_data.append(matching_objects)

final_grouped_data = []

for unique_name in unique_names_array:
    instructor = unique_name.get("Instructor")
    course = unique_name.get("Course")

    matching_objects = [entry for entry in data if
                        entry.get("Instructor") == instructor and entry.get("Course") == course]

    # Combine department, discipline, course, and instructor
    combined_info = {
        "Department": matching_objects[0].get("Department"),
        "Discipline": matching_objects[0].get("Discipline"),
        "Course": course,
        "Instructor": instructor
    }

    # Create a list of sections
    sections = []
    for obj in matching_objects:
        section_info = {
            "Section": obj.get("Section"),
            "A": obj.get("A"),
            "B": obj.get("B"),
            "C": obj.get("C"),
            "D": obj.get("D"),
            "F": obj.get("F"),
            "P": obj.get("P"),
            "NP": obj.get("NP"),
            "IX": obj.get("IX"),
            "SP": obj.get("SP"),
            "W": obj.get("W"),
            "EW": obj.get("EW"),
            "TotalCount": obj.get("TotalCount")
        }
        sections.append(section_info)

    combined_info["Sections"] = sections

    final_grouped_data.append(combined_info)

output_file = 'final.json'

# Write the grouped data to a JSON file
with open(output_file, 'w') as json_file:
    json.dump(final_grouped_data, json_file, indent=4)

print(f'Grouped data has been saved to JSON file "{output_file}"')

