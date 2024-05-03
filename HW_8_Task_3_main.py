"""
Соберите из созданных на уроке и в рамках домашнего задания функций пакет  для работы с файлами разных форматов.
"""
import file_utils

# Чтение CSV файла
csv_data = file_utils.csv_utils.read_csv('data.csv')

# Запись JSON файла
json_data = {'key': 'value'}
file_utils.json_utils.write_json('data.json', json_data)

# Чтение Pickle файла
pickle_data = file_utils.pickle_utils.read_pickle('data.pickle')

# Создание структуры файлов
file_utils.structure_utils.create_structure_files('/path/to/directory', '/path/to/output')
