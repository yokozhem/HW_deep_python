"""
3. Добавьте в пакет, созданный на семинаре шахматный модуль. 
Внутри него напишите код, решающий задачу о 8 ферзях. 
Известно, что на доске 8×8 можно расставить 8 ферзей так, 
чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, определите, 
есть ли среди них пара бьющих друг друга. 
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. 
Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
"""


# Шахматный модуль

# HW_6_Task_3.py

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
            if queens[i][0] == queens[j][0] or queens[i][1] == queens[j][1] or abs(queens[i][0] - queens[j][0]) == abs(queens[i][1] - queens[j][1]):
                return False
    return True

def are_queens_safe_with_conflicts(queens):
    """
    Проверяет, не бьют ли ферзи друг друга на заданной расстановке.
    Возвращает пару, содержащую True, если ферзи не бьют друг друга, и пустой список конфликтующих ферзей,
    и False в противном случае, вместе с списком пар координат бьющих друг друга ферзей.

    Args:
        queens (list): Список координат ферзей на доске.

    Returns:
        tuple: Пара из булевого значения и списка пар координат бьющих друг друга ферзей.
    """
    conflicting_queens = []
    # Проверяем каждую пару ферзей
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            # Проверяем, бьют ли ферзи друг друга
            if (
                queens[i][0] == queens[j][0] 
                or queens[i][1] == queens[j][1] 
                or abs(queens[i][0] - queens[j][0]) == abs(queens[i][1] - queens[j][1])
            ):
                conflicting_queens.append((queens[i], queens[j]))

    if conflicting_queens:
        return False, conflicting_queens
    else:
        return True, []

if __name__ == "__main__":
    # Тестирование функции
    queens = [(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (8, 8)]
    safe, conflicts = are_queens_safe_with_conflicts(queens)
    if safe:
        print("Ферзи не бьют друг друга")
    else:
        print("Ферзи бьют друг друга. Конфликтующие ферзи:", conflicts)
