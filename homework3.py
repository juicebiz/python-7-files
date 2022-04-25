import os

FILES_DIR = 'sorted'
RESULT_FILE = 'result.txt'

def get_files_dict(files_dir: str = FILES_DIR):
    files = os.listdir(files_dir)
    quantity_strings = {}
    for file in files:
        quantity = get_quantity_lines_in_file(files_dir, file)
        quantity_strings[file] = quantity
    sorted_files = dict(sorted(quantity_strings.items(), key=lambda item: item[1]))
    return sorted_files

def get_quantity_lines_in_file(files_dir: str, file_name: str):
    count = 1
    path = os.path.join(files_dir,file_name)
    with open(path, 'r', encoding = 'utf-8') as file:
        for line in file:
            count += 1
    return count

def summary_file(files_dir: str = FILES_DIR, result_file_name: str = RESULT_FILE):
    files = get_files_dict(files_dir)
    if os.path.exists(result_file_name):
        os.remove(result_file_name)
    with open(result_file_name, 'a', encoding = 'utf-8') as file_result:
        for file_name in files:
            path = os.path.join(files_dir, file_name)
            with open(path, 'r', encoding = 'utf-8') as file:
                file_result.write(file_name + '\n')
                file_result.write(str(files[file_name]) + '\n')
                file_result.write(file.read().strip() + '\n')

summary_file()