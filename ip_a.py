from pprint import pprint
with open('ip_a.txt', 'r', encoding='utf8') as f:
    fioLst = []
    ipALst = dict()
    for line in f:
        fio, ipA = line.split('\t')
        ipALst.update({ipA[:-1]: fio.split()})
pprint(ipALst)
'''
vvod = input("Введите фамилию и инициалы? ")
Vvod = vvod.split()
last = next(reversed(ipALst))
for key, value in ipALst.items():
    if value[0] == Vvod[0] and value[1][0] == Vvod[1][0] and value[2][0] == Vvod[1][1]:
        print(f"{key}: {' '.join(value)} ")
        break
    elif key != last:
        continue
    else:
        print(f"{vvod}: сведения отсутствуют")
'''