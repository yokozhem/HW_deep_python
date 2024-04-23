"""
2. Напишите функцию группового переименования файлов. Она должна:
a. принимать параметр желаемое конечное имя файлов. 
   При переименовании в конце имени добавляется порядковый номер.
b. принимать параметр количество цифр в порядковом номере.
c. принимать параметр расширение исходного файла. 
   Переименование должно работать только для этих файлов внутри каталога.
d. принимать параметр расширение конечного файла.
e. принимать диапазон сохраняемого оригинального имени. 
   Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
   К ним прибавляется желаемое конечное имя, если оно передано. 
   Далее счётчик файлов и расширение."""

import os

def get_files_with_extension(directory, extension):
    """
    Получает список файлов в указанном каталоге с заданным расширением.

    Args:
        directory (str): Путь к каталогу.
        extension (str): Расширение файлов.

    Returns:
        list: Список файлов с заданным расширением в указанном каталоге.
    """
    files = []
    for file in os.listdir(directory):
        if file.endswith(extension):
            files.append(file)
    return files
def group_rename_files(directory, extension, desired_name, digits, new_extension, name_range=None):
    """
    Выполняет групповое переименование файлов.

    Args:
        directory (str): Путь к каталогу.
        extension (str): Расширение исходных файлов.
        desired_name (str): Желаемое конечное имя файлов.
        digits (int): Количество цифр в порядковом номере.
        new_extension (str): Расширение конечного файла.
        name_range (tuple, optional): Диапазон сохраняемого оригинального имени.

    Returns:
        None
    """
    files = get_files_with_extension(directory, extension)
    if not files:
        print("Нет файлов с заданным расширением в указанном каталоге.")
        return

    for i, file in enumerate(files, start=1):
        original_name = file if name_range is None else file[name_range[0]-1:name_range[1]]
        new_name = f"{desired_name}{i:0{digits}d}.{new_extension}"
        os.rename(os.path.join(directory, file), os.path.join(directory, new_name))
        print(f"Файл {file} переименован в {new_name}")


group_rename_files("/Users/pelmeshka/Documents/Обучение/Python погружение/доки", ".xlsx", "Тест переименования", 3, "new_чдыч", (3, 6))
