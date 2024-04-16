"""
2. Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. 
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
"""

import os

def parse_file_path(file_path):
    path, filename = os.path.split(file_path)
    filename, extension = os.path.splitext(filename)
    return path, filename, extension

# Пример использования
file_path = "/Users/pelmeshka/Documents/Обучение/Python погружение/pptx"
result = parse_file_path(file_path)
print(result)
