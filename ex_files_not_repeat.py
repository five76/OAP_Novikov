"""

Записать в файл f N целых чисел, полученных с помощью генератора случайных чисел.
Из файла f получить файл g, исключив повторное вхождение чисел
"""


def find_not_repeat(file_name_input, file_name_output):
    a = set()
    with open(file_name_input) as f, open(file_name_output, 'w') as g:
        for line in f:
            a.add(line)
        g.writelines(list(a))

if __name__ == '__main__':

    import random

    n = 100      # количество чисел
    with open('random_number.txt', 'w') as f:
        for i in range(n):
            f.write(str(random.randint(1, 50))+'\n')
