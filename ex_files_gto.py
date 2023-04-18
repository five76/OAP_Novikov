"""
В файле input_data_gto.txt записаны ФИО студентов, возраст, пол и количество отжиманий при сдаче норм ГТО
Вывест список  студентов c присвоенным им статусом 'g - gold', 's-silver', 'b-bronze', '0 - zero', исходя з нормативов,
представленных в файле НормыГТО.pdf

input_data_gto.txt:
Иванов Иван Иванович 19 м 25
Петрова Наталья Ивановна 18 ж 15
...

Output:
Иванов Иван s
Петрова Наталья s
...
"""

def gto_men(age,ot):
    if 17<age<25:
        if ot<28:
            return '0'
        if 28<=ot<32:
            return 'b'
        elif 32<=ot<44:
            return 's'
        else:
            return 'g'
    else:
        if ot < 22:
            return '0'
        if 22 <= ot < 25:
            return 'b'
        elif 25 <= ot < 39:
            return 's'
        else:
            return 'g'


def gto_women(age,ot):
    return '0'
    #print('Women', age, ot)

with open('input_data_gto.txt', encoding='utf8') as f:
    for line in f:
        data_lst = line.split()
        if data_lst[4] == 'м':
            status = gto_men(int(data_lst[3]), int(data_lst[5]))
        else:
            status =  gto_women(int(data_lst[3]), int(data_lst[5]))

        print(f'{data_lst[0]} {data_lst[1]} {status}')