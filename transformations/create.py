import pandas as pd
import json


def create_class_lists(file_path):
    complete_json_file = file_path.split("_cleaned.csv")[0] + ".json"

    df = pd.read_csv(file_path)
    data_list = df.to_dict(orient='records')

    unique_course_and_instructors_set = set()

    for data in data_list:
        instructor = data.get("Instructor")
        course = data.get("Course")

        if instructor and course:
            unique_course_and_instructors_set.add((instructor, course))

    unique_course_and_instructors = [{"Instructor": instructor, "Course": course}
                                     for instructor, course in unique_course_and_instructors_set]

    final_data = []

    for unique_data in unique_course_and_instructors:
        instructor = unique_data.get("Instructor")
        course = unique_data.get("Course")

        matching_data = [data for data in data_list
                         if data.get("Instructor") == instructor and data.get("Course") == course]

        combined_a = 0.0
        combined_b = 0.0
        combined_c = 0.0
        combined_d = 0.0
        combined_f = 0.0
        combined_p = 0.0
        combined_np = 0.0
        combined_ix = 0.0
        combined_rd = 0.0
        combined_sp = 0.0
        combined_w = 0.0
        combined_ew = 0.0
        combined_total = 0.0

        for data in matching_data:
            combined_a = data.get("A") + combined_a
            combined_b = data.get("B") + combined_b
            combined_c = data.get("C") + combined_c
            combined_d = data.get("D") + combined_d
            combined_f = data.get("F") + combined_f
            combined_p = data.get("P") + combined_p
            combined_np = data.get("NP") + combined_np
            combined_ix = data.get("IX") + combined_ix
            combined_rd = data.get("RD") + combined_rd
            combined_sp = data.get("SP") + combined_sp
            combined_w = data.get("W") + combined_w
            combined_ew = data.get("EW") + combined_ew
            combined_total = data.get("Total") + combined_total

        combined_course_info = {
            "department": matching_data[0].get("Department"),
            "discipline": matching_data[0].get("Discipline"),
            "course": course,
            "instructor": instructor,
            "total_a": combined_a,
            "total_b": combined_b,
            "total_c": combined_c,
            "total_d": combined_d,
            "total_f": combined_f,
            "total_p": combined_p,
            "total_np": combined_np,
            "total_ix": combined_ix,
            "total_rd": combined_rd,
            "total_sp": combined_sp,
            "total_w": combined_w,
            "total_ew": combined_ew,
            "total_students": combined_total
        }

        sections = []
        for data in matching_data:
            section_info = {
                "section": data.get("Section"),
                "a": data.get("A"),
                "b": data.get("B"),
                "c": data.get("C"),
                "d": data.get("D"),
                "f": data.get("F"),
                "p": data.get("P"),
                "np": data.get("NP"),
                "ix": data.get("IX"),
                "sp": data.get("SP"),
                "w": data.get("W"),
                "ew": data.get("EW"),
                "total": data.get("Total")
            }
            sections.append(section_info)

        combined_course_info['sections'] = sections

        final_data.append(combined_course_info)

    with open(complete_json_file, 'w') as json_file:
        json.dump(final_data, json_file, indent=4)

    print(f"Formatted JSON file saved to {complete_json_file}")