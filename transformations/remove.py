import os


def all_other_files(directory):
    for root, dirs, files in os.walk(directory, topdown=False):
        for file in files:
            if not file.endswith('.xlsx'):
                file_path = os.path.join(root, file)
                os.remove(file_path)

        for dir in dirs:
            dir_path = os.path.join(root, dir)
            os.rmdir(dir_path)
    print(f"{directory} folder has been cleaned.")