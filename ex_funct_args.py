def print_number(a,b):
    print('Работает функция print_number')
    print(a)
    print(b)


def print_number1(a=0,b=0):
    print('Работает функция print_number1')
    print(a)
    print(b)


def print_number2(*args):
    print(args)


def print_number3(**kwargs):
    print(kwargs)

if __name__ == '__main__':
    print('Начало')
    a = 10
    k = 5
    print_number(a, k)
    print_number(k, a)
    print_number1()
    print_number1(b=12, a=3)
    print_number1(a,k)

    print_number2(1,2,3)

    print_number3(z=1,x=2,c=3)

    print('Конец')
