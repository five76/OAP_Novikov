"""
В файле input_data.txt записаны ФИО студентов и оценки по предмету.
Составить программу, для подсчта среднего балла каждого студента

input_data.txt:
Иванов Иван Иванович 4,5,3,5,4
Петров Петр Петрович 4,4,5,3,4,5,4
...

Output:
Иванов И.И. 4.2
Петров П.П. ...
...

"""

with open('input_data.txt', encoding='utf8') as f:
    for line in f:
        #print(line, end='')
        fio_lst = line.split()
        #print(fio_lst)
        fio = fio_lst[0] + ' ' + fio_lst[1][0] + '.' + fio_lst[2][0] + '. '
        ball_lst = fio_lst[3].split(',')
        s = 0 # сумма баллов
        for i in ball_lst:      #для каждого балла i из всех баллов
            s += int(i)         #увеличиваем сумму на целочисленное значение i
        ball_avg = s / len(ball_lst)
        print(f'{fio} {ball_avg:.2f}')