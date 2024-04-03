"""" Задача 4. Программа загадывает число от 0 до 1000. 
Необходимо угадать число за 10 попыток. 
Программа должна подсказывать “больше” или “меньше” после каждой попытки. 
Для генерации случайного числа используйте код:
from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT) """

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
MAX_ATTEMPTS = 10

# Генерируем случайное число от 0 до 1000
secret_number = randint(LOWER_LIMIT, UPPER_LIMIT)

print("Программа загадала число от 0 до 1000. У вас 10 попыток, чтобы его угадать.")

for attempt in range(MAX_ATTEMPTS):
    guess = int(input(f"Попытка {attempt + 1}. Угадайте число: "))
    
    if guess == secret_number:
        print("Поздравляем! Вы угадали число.")
        break
    elif guess < secret_number:
        print("Загаданное число больше.")
    else:
        print("Загаданное число меньше.")
else:
    print(f"Вы проиграли! Загаданное число было {secret_number}.")
