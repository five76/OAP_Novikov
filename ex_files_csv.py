import csv

with open('host_data.csv') as f:
    reader = csv.reader(f, delimiter=';')
    head = next(reader)

    a, b, c, d = head
    print('{:^10s} {:^16s} {:^10s} {:^16s}'.format(a,b,c,d))
    for row in reader:
        a, b, c, d = row
        print('{:^10s} {:^16s} {:^10s} {:^16s}'.format(a, b, c, d))

