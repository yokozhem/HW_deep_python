""" 3. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions
"""

from fractions import Fraction

def operate_fractions(fraction1, fraction2):
    # Преобразование строковых представлений в объекты Fraction
    frac1 = Fraction(fraction1)
    frac2 = Fraction(fraction2)

    # Сумма и произведение дробей
    sum_result = frac1 + frac2
    product_result = frac1 * frac2

    return sum_result, product_result

def main():
    # Ввод двух дробей в формате "a/b"
    fraction1 = input("Введите первую дробь (в формате 'a/b'): ")
    fraction2 = input("Введите вторую дробь (в формате 'a/b'): ")

    # Выполнение операций с дробями
    sum_result, product_result = operate_fractions(fraction1, fraction2)

    # Вывод результатов
    print("Сумма дробей:", sum_result)
    print("Произведение дробей:", product_result)

if __name__ == "__main__":
    main()
