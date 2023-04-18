import csv
with open('electro.csv') as f:
    reader = csv.reader(f, delimiter=';')
    next(reader)
    sum_potr = {}
    ss = 0
    for row in reader:
        fio, *e = row
        e_1 = [int(x) for x in e]
        ss += sum(e_1)
        print(f'{fio} {sum(e_1)} КВт')
        sum_potr[fio] = sum(e_1)
print(sum_potr)

