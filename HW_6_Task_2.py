"""
В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
"""

from datetime import datetime
import sys

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def is_valid_date(date_str):
    try:
        date = datetime.strptime(date_str, '%d.%m.%Y')
        print(f"Дата {date_str} допустима")
        if is_leap_year(date.year):
            print(f"Год {date.year} високосный")
        else:
            print(f"Год {date.year} не високосный")
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python date_checker.py DD.MM.YYYY")
    else:
        date_to_check = sys.argv[1]
        if is_valid_date(date_to_check):
            print("Допустимая дата")
        else:
            print("Недопустимая дата")

