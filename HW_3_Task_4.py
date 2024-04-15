""" 4. Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
Достаточно вернуть один допустимый вариант.*Верните все возможные варианты комплектации рюкзака.
"""

def backpack(items, max_weight):
    # Функция для поиска всех возможных комбинаций вещей, которые могут поместиться в рюкзак

    def backpack_recursive(items, max_weight, index, current_weight, current_items, result):
        # Базовый случай: если текущий индекс равен длине списка вещей
        # или текущий вес превышает максимальный вес, добавляем текущую комбинацию в результирующий список
        if index == len(items) or current_weight > max_weight:
            result.append(current_items)
            return
        
        # Вариант 1: не включаем текущий предмет в комбинацию
        backpack_recursive(items, max_weight, index + 1, current_weight, current_items, result)
        
        # Вариант 2: включаем текущий предмет в комбинацию, если его вес не превышает максимальный вес
        if current_weight + items[index][1] <= max_weight:
            backpack_recursive(items, max_weight, index + 1, current_weight + items[index][1], current_items + [items[index]], result)
    
    # Инициализация списка для хранения результатов
    result = []
    # Вызов вспомогательной функции
    backpack_recursive(items, max_weight, 0, 0, [], result)
    return result

# Пример использования функции
items = {
    'спальник': 2,
    'еда': 3,
    'палатка': 4,
    'фонарь': 1
}
max_weight = 6
possible_combinations = backpack(list(items.items()), max_weight)
print("Все возможные варианты комплектации рюкзака:")
for combination in possible_combinations:
    print(combination)
