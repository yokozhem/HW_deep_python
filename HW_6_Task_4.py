"""
4. Напишите функцию в шахматный модуль. 
Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. 
Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
"""
from random import sample
from HW_6_Task_3 import are_queens_safe_with_conflicts


# Генерация случайных расстановок ферзей с возвратом конфликтующих ферзей
def generate_queens_arrangement_with_conflicts():
    """
    Генерирует 4 случайные расстановки ферзей на доске 8x8.
    Возвращает кортеж, содержащий успешные расстановки и списки конфликтующих ферзей для каждой расстановки.

    Returns:
        tuple: Кортеж из двух элементов. Первый элемент - список успешных расстановок ферзей.
               Второй элемент - список списков пар координат бьющих друг друга ферзей для каждой расстановки.
    """
    arrangements = []
    conflicts_list = []  # список для хранения списков пар координат бьющих друг друга ферзей
    for _ in range(4):
        queens = [(i, j) for i in range(1, 9) for j in range(1, 9)]
        arrangement = sample(queens, 8)
        arrangements.append(arrangement)
        safe, conflicts = are_queens_safe_with_conflicts(arrangement)
        if not safe:
            conflicts_list.append(conflicts)
    return arrangements, conflicts_list

# Проверка успешных расстановок
if __name__ == "__main__":
    arrangements, conflicts_list = generate_queens_arrangement_with_conflicts()
    if not arrangements:
        print("Не удалось найти безопасные расстановки ферзей")
    else:
        print("Все расстановки ферзей:")
        for i, arrangement in enumerate(arrangements, start=1):
            print(f"Расстановка {i}: {arrangement}")
            for queen in arrangement:
                print(queen)
            print()

            if i <= len(conflicts_list):
                conflicts = conflicts_list[i - 1]
                if conflicts:
                    print("Конфликтующие ферзи:")
                    for conflict in conflicts:
                        print(f"Ферзь на позиции {conflict[0]} бьет ферзя на позиции {conflict[1]}")
                else:
                    print("Расстановка безопасна")
            else:
                print("Расстановка безопасна")
            print()
