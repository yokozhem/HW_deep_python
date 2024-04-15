""" 2. Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. 
В результирующем списке не должно быть дубликатов. """

def remove_duplicates(input_list):
    # Преобразование списка во множество, чтобы удалить дубликаты
    unique_set = set(input_list)
    # Преобразование множества обратно в список
    unique_list = list(unique_set)
    return unique_list

# Пример использования функции
input_list = [1, 2, 2, 3, 4, 4, 5]
result_list = remove_duplicates(input_list)
print("Результирующий список без дубликатов:", result_list)
