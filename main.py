from transformations import collect_files, delete_all_other_files, convert_xlsx_to_csv, clean_csv, create_class_lists

def run_transformations(file_path):
    print(f"Running transformation on: {file_path}")
    csv_file_path = convert_xlsx_to_csv(file_path)
    cleaned_csv_file_path = clean_csv(csv_file_path)
    create_class_lists(cleaned_csv_file_path)
    print(f"Finished transformation on: {file_path}\n")


def main():
    dir = "grades"
    delete_all_other_files(dir)
    file_paths = collect_files(dir)
    for file_path in file_paths:
        run_transformations(file_path)


if __name__ == "__main__":
    main()
