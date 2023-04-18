ip_lst = ['192.168.10.12/24',
          '192.168.10.85/24',
          '192.168.20.85/24',
          '172.16.10.32/26',
          '172.16.10.81/26',
          ]

print("|", "-" * 39, "|")
print("| {0:^39}".format("Addresses Table") + " |")
print("|", "-" * 39, "|")

template = "| {0:^17} | {1:^19} |"

print(template.format('IP', 'MASK'))
print("|", "-" * 39, "|")

for i in ip_lst:
    if i.split('/')[1] == "24":
        i.split('/')[1] = "255.255.255.0"
    elif i.split('/')[1] == "26":
        i.split('/')[1] = "255.255.255.128"
    print(template.format(i.split('/')[0], i.split('/')[1]))

print("|", "-" * 39, "|")