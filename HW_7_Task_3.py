"""
Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.
"""
import os
import random
import shutil

def generate_file(file_path, num_lines, line_length):
    with open(file_path, 'w') as file:
        for _ in range(num_lines):
            line = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(line_length))
            file.write(line + '\n')

def sort_files(source_dir, dest_dir):
    file_types = {
        'images': ['.jpg', '.jpeg', '.png', '.gif'],
        'videos': ['.mp4', '.avi', '.mkv'],
        'documents': ['.txt', '.pdf', '.docx'],
        'others': []
    }

    os.makedirs(dest_dir, exist_ok=True)

    for file in os.listdir(source_dir):
        for category, extensions in file_types.items():
            for ext in extensions:
                if file.endswith(ext):
                    category_dir = os.path.join(dest_dir, category)
                    os.makedirs(category_dir, exist_ok=True)
                    shutil.move(os.path.join(source_dir, file), os.path.join(category_dir, file))
                    break
        else:
            shutil.move(os.path.join(source_dir, file), os.path.join(dest_dir, 'others', file))

def rename_file(file_path, new_name):
    dir_path, old_name = os.path.split(file_path)
    new_file_path = os.path.join(dir_path, new_name)
    os.rename(file_path, new_file_path)

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def write_to_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)
