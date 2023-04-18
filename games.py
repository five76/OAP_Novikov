
'''
Определить жанр, лидирующий по продажам в каждом регионе
'''
import csv
from pprint import pprint

from colorama import init as colorama_init
from colorama import Fore
from colorama import Style


def sorted_genre(d):

    """
    Сортировка словаря по убыванию значений
    :param d: Словарь для сортировки
    :return:
    """
    sorted_tuple = sorted(d.items(), key=lambda x: x[1],reverse=True)
    return dict(sorted_tuple)


def find_top_genre(df):
    """
    Формирование словарей с суммарными значениями для жанров по каждому региону
    :param df:
    :return:
    """
    for row in df[1:]:
        g = row[3]
        if g not in us.keys() and \
                g not in eu.keys() and \
                g not in jp.keys() and \
                g not in ot.keys():
            us[g] = float(row[4])
            eu[g] = float(row[5])
            jp[g] = float(row[6])
            ot[g] = float(row[7])
        else:
            us[g] = us[g] + float(row[4])
            eu[g] = eu[g] + float(row[5])
            jp[g] = jp[g] + float(row[6])
            ot[g] = ot[g] + float(row[7])

    print('-' * 80)
    print(sorted_genre(us))
    print(sorted_genre(eu))
    print(sorted_genre(jp))
    print(sorted_genre(ot))
    print('-' * 80)
    print(f'US - {list(sorted_genre(us).keys())[0]}')
    print(list(sorted_genre(eu).keys())[0])
    print(list(sorted_genre(jp).keys())[0])
    print(list(sorted_genre(ot).keys())[0])


def print_dict(*args):
    """
    Печать словарей в виде таблицы
    :param args:
    :return:
    """
    kk = set()
    for i in args:
        p = list(i.keys())
        kk = kk | set(p)
    kk = list(kk)
    for i in sorted(kk):
        print(f'{i:15}', end=' ')

        for j in args:
            print(f'{j[i]:8.1f}', end=' ')
        print()
        #print('\n','-'*(len(args)*9+15))

genre = {}
us = {}
eu = {}
jp = {}
ot = {}

#формирование списка с данными
df = []
with open('games.csv') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        df.append(row)

find_top_genre(df)
print_dict(us,eu,jp,ot)

