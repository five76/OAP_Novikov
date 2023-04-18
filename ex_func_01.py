def say_hello(name):
    print(f"Здравствуйте, {name}")

def say_hello_ip(name,ip):
    print(f"Здравствуйте, {name}. Ваш ip-адрес {ip}")

def msg_ex_traffic (name,packet,fact,price):
    if fact > packet:
        diff_traffic = fact - packet
        payment = diff_traffic * price
        print (f'{name}, вы должны доплатить {payment} руб.')
    else:
        print(f'{name}, мы рады сотрудичеству с вами')



#say_hello('Dmitry')
#say_hello('Иван')

list_empl = ['Дмитрий', 'Иван', 'Анастасия', 'Валерий']
list_ip_addr = ['10.10.10.1', '10.10.10.2', '10.10.10.3', '10.10.10.4']
list_packet = [100, 50, 60, 80]
list_fact_gb = [98, 55, 69, 77]
price = 10.5

'''
for name in list_empl:
    say_hello(name)
'''

for i in range(0,len(list_empl)):
    #say_hello_ip(list_empl[i],list_ip_addr[i])
    msg_ex_traffic(list_empl[i],list_packet[i],list_fact_gb[i],price)