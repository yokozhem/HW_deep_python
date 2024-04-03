"""" Задача 3. Напишите код, который запрашивает число и сообщает является ли оно простым или составным. 
Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
 Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч. """

user_input = input("Введите число (ограничение от 0 до 100000): ")

if not user_input.isdigit():
    print("Ошибка: Число должно быть в диапазоне от 0 до 100000")
elif int(user_input) < 0 or int(user_input) > 100000:
    print("Число должно быть в диапазоне от 0 до 100000.")
else:
    number = int(user_input)
    if number <= 1:
        print("Число", number, "является составным.")
    else:
        is_prime = True
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            print("Число", number, "является простым.")
        else:
            print("Число", number, "является составным.")
