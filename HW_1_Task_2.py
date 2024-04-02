""" Задача 2. Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. 
Дано a, b, c - стороны предполагаемого треугольника. 
Требуется сравнить длину каждого отрезка-стороны с суммой двух других. 
Если хотя бы в одном случае отрезок окажется больше суммы двух других, 
то треугольника с такими сторонами не существует. 
Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним. """

a = int(input("Введите сторону a: \n"))
b = int(input("Введите сторону b: \n"))
c = int(input("Введите сторону c: \n"))

if a >= b + c or b>= a + c or c >= a + b:
    print('Ой, кажется такой треугольник не существует')
else:
    if a != b and a != c and b != c:
        print("Этот треугольник разносторонний")
    elif a == b and a == c:
        print("Этот треугольник равносторонний")
    else:
        print("Этот треугольник равнобедренный")
