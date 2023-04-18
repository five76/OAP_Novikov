
'''
Определить жанр, лидирующий по продажам в каждом регионе
'''
import csv
from pprint import pprint

from colorama import init as colorama_init
from colorama import Fore
from colorama import Style



#формирование списка с данными
df = []
with open('covid.csv') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        df.append(row)
print(df)
#find_top_genre(df)
#print_dict(us,eu,jp,ot)

