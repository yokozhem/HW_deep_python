"""
Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. 
Результаты обхода сохраните в файлы json, csv и pickle. 
Для дочерних объектов указывайте родительскую директорию. 
Для каждого объекта укажите файл это или директория.
Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
"""
import os
import json
import csv
import pickle

def get_directory_size(directory):
    total_size = 0
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            total_size += os.path.getsize(filepath)
    return total_size

def create_directory_structure(directory):
    structure = []
    for dirpath, dirnames, filenames in os.walk(directory):
        directory_info = {
            "name": os.path.basename(dirpath),
            "type": "directory",
            "path": dirpath,
            "size": get_directory_size(dirpath)
        }
        structure.append(directory_info)
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            file_info = {
                "name": filename,
                "type": "file",
                "path": dirpath,
                "size": os.path.getsize(filepath)
            }
            structure.append(file_info)
    return structure

def save_structure_to_json(structure, json_file):
    with open(json_file, "w") as f:
        json.dump(structure, f, indent=4)

def save_structure_to_csv(structure, csv_file):
    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "type", "path", "size"])
        writer.writeheader()
        for item in structure:
            writer.writerow(item)

def save_structure_to_pickle(structure, pickle_file):
    with open(pickle_file, "wb") as f:
        pickle.dump(structure, f)

def create_structure_files(directory, output_dir):
    structure = create_directory_structure(directory)
    json_file = os.path.join(output_dir, "structure.json")
    csv_file = os.path.join(output_dir, "structure.csv")
    pickle_file = os.path.join(output_dir, "structure.pickle")
    save_structure_to_json(structure, json_file)
    save_structure_to_csv(structure, csv_file)
    save_structure_to_pickle(structure, pickle_file)

if __name__ == "__main__":
    directory_path = "/Users/pelmeshka/Documents/Обучение/Python погружение"
    output_directory = "/Users/pelmeshka/Documents/Обучение/Python погружение/HW"
    create_structure_files(directory_path, output_directory)
