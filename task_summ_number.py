import random

def sum_digits_number(d):
    result = 1
    while d >= 1:
        n = d % 10          # выделяем последнюю цифру
        result += n         # увеличиваем сумму
        d = d//10           # переопределяем число
    return result

d = random.randint(1000, 9999)  # генерируем случайное число
print(f'Сумма цифр числа {d} равна {sum_digits_number(d)}')