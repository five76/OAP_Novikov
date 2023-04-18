"""

Записать в файл N целых чисел, полученных с помощью генератора случайных чисел.
Вычислить сумму всех элементов файла.
"""


def sum_number_in_file(file_input):
    """

    Нахождение суммы
    :param file_input: Имя файла с числами
    :return:
    """

    s = 0
    with open(file_input) as f:
        for number in f:  # считываем строку
            s += int(number)  # преобразуем строку в целое число и добавляем к сумме
    return s


def find_multiple(file_name_input,file_name_output,m):
    with open(file_name_input) as f_in, open(file_name_output, 'w') as f_out:
        for line in f_in:
            if int(line) % m == 0:
                f_out.write(line)


import random
n = 10      # количество чисел

with open('random_number.txt', 'w') as f:
    for i in range(n):
        f.write(str(random.randint(1, 100))+'\n')


# Нахождение суммы
print(f'Сумма всех элементов файла равна \
        {sum_number_in_file("random_number.txt")}')



find_multiple('random_number.txt','number_multiple',5)


