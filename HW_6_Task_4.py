"""
4. Напишите функцию в шахматный модуль. 
Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. 
Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
"""
from HW_6_Task_3 import are_queens_safe
from random import sample


# Шахматный модуль

def are_queens_safe(queens):
    """
    Проверяет, не бьют ли ферзи друг друга на заданной расстановке.

    Args:
        queens (list): Список координат ферзей на доске.

    Returns:
        bool: True, если ферзи не бьют друг друга, иначе False.
    """
    # Проверяем каждую пару ферзей
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            # Проверяем, бьют ли ферзи друг друга по горизонтали, вертикали или диагонали
            if (
                queens[i][0] == queens[j][0]
                or queens[i][1] == queens[j][1]
                or abs(queens[i][0] - queens[j][0]) == abs(queens[i][1] - queens[j][1])
            ):
                return False
    return True

# Генерация случайных расстановок ферзей
def generate_queens_arrangement():
    """
    Генерирует 4 случайные безопасные расстановки ферзей на доске 8x8.

    Returns:
        list: Список успешных расстановок ферзей.
    """
    arrangements = []
    for _ in range(4):
        queens = [(i, j) for i in range(1, 9) for j in range(1, 9)]
        arrangement = sample(queens, 8)
        if are_queens_safe(arrangement):
            arrangements.append(arrangement)
    return arrangements

# Проверка успешных расстановок
if __name__ == "__main__":
    arrangements = generate_queens_arrangement()
    if not arrangements:
        print("Не удалось найти безопасные расстановки ферзей")
    else:
        print("Все расстановки ферзей:")
        for i, arrangement in enumerate(arrangements, start=1):
            print(f"Расстановка {i}: {arrangement}")
            for queen in arrangement:
                print(queen)
            print()

        print("Проверка безопасности расстановок:")
        for i, arrangement in enumerate(arrangements, start=1):
            print(f"Расстановка {i}: {'безопасна' if are_queens_safe(arrangement) else 'не безопасна'}")
