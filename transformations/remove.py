import os
import glob


# def ds_store_files(directory):
#     for root, dirs, files in os.walk(directory):
#         for file in files:
#             if file == '.DS_Store':
#                 file_path = os.path.join(root, file)
#                 os.remove(file_path)
#                 print(f"Removed: {file_path}")

def all_other_files(directory):
    all_files = os.listdir(directory)

    # Use glob to filter for .xlsx files
    xlsx_files = glob.glob(os.path.join(directory, '*.xlsx'))

    # Iterate through all files and remove those that are not .xlsx files
    for file in all_files:
        file_path = os.path.join(directory, file)

        # Check if the file is not an .xlsx file
        if file_path not in xlsx_files:
            try:
                os.remove(file_path)
                print(f"Removed: {file_path}")
            except Exception as e:
                print(f"Error removing {file_path}: {str(e)}")