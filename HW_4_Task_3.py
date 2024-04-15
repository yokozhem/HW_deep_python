"""
3. Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. 
Дополнительно сохраняйте все операции поступления и снятия средств в список.
"""

from decimal import Decimal

# Constants
PROCENT_COMMISION = Decimal('0.015')  # Commission as a percentage
MIN_SUM = Decimal('50')  # Minimum sum
MIN_COMISSION = Decimal('30')  # Minimum commission
MAX_COMISSION = Decimal('600')  # Maximum commission

# List to store transactions
transactions = []

def get_money(balance: Decimal) -> Decimal:
    """
    Функция для снятия средств со счета.

    Аргументы:
    balance (Decimal): Текущий баланс.

    Возвращает:
    Decimal: Новый баланс после снятия средств.
    """
    money_to_get = Decimal(input('Введите сумму снятия: '))
    procent = money_to_get * PROCENT_COMMISION

    if money_to_get % MIN_SUM == 0:
        if procent < MIN_COMISSION:
            procent = MIN_COMISSION
        elif procent > MAX_COMISSION:
            procent = MAX_COMISSION

        if money_to_get + procent <= balance:
            transactions.append((-money_to_get, balance - (money_to_get + procent)))
            balance -= (money_to_get + procent)
            return balance, True
        else:
            print('Недостаточно средств для снятия')
            print()
            return balance, False

    else:
        print('Ошибка снятия денег, сумма должна быть кратна 50')
        print()
        return balance, False


def give_money(balance: Decimal) -> Decimal:
    """
    Функция для пополнения счета.

    Аргументы:
    balance (Decimal): Текущий баланс.

    Возвращает:
    Decimal: Новый баланс после пополнения счета.
    """
    money_to_give = Decimal(input('Введите сумму пополнения: '))

    if money_to_give % MIN_SUM == 0:
        transactions.append((money_to_give, balance + money_to_give))
        balance += money_to_give
        return balance, True
    else:
        print('Недостаточно средств для пополнения, сумма не кратна 50')
        print()
        return balance, False


def show_transactions():
    """
    Функция для отображения списка операций.
    """
    print("Список операций:")
    for transaction in transactions:
        amount, balance = transaction
        if amount < 0:
            print(f"Снятие {abs(amount)} у.е., баланс после операции: {balance}")
            print()
        else:
            print(f"Пополнение {amount} у.е., баланс после операции: {balance}")
            print()


def menu(balance: Decimal):
    """
    Функция для отображения меню.

    Аргументы:
    balance (Decimal): Текущий баланс.
    """
    print("1. Пополнить счет")
    print("2. Снять деньги")
    print("3. Показать баланс")
    print("4. Показать список операций")
    print("5. Выйти")
    print()
    


if __name__ == '__main__':
    print('Добро пожаловать в программу банкомат')
    print()
    balance = Decimal('0')
    isFlag = True
    while isFlag:
        menu(balance)
        choice = input('Выберите действие: ')
        if choice == '1':
            balance, success = give_money(balance)
            if success:
                print(f'Остаток на счете: {balance}')
                print()
        elif choice == '2':
            balance, success = get_money(balance)
            if success:
                print(f'Остаток на счете: {balance}')
                print()
        elif choice == '3':
            print(f'Остаток на счете: {balance}')
            print()
        elif choice == '4':
            show_transactions()
            print()
        elif choice == '5':
            print('До свидания!')
            print()
            isFlag = False
        else:
            print('Некорректный выбор. Пожалуйста, выберите снова.')
            print()
