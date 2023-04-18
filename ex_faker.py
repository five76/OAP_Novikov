import random
from faker import Faker


def last_digit(n):
    result = n % 10
    return result

def first_digits(n):
    result = n//10
    return result

def first_last_digits(n):
    ld = n % 10
    fd = n // 10
    return ld, fd

for i in range(10):
    number = random.randint(1000,10000)
    ld = last_digit(number)
    fd = first_digits(number)
    ld1, fd1 = first_last_digits(number)
    print(fd, ld, '-----', fd1, ld1)

mock = Faker('ru_RU')
for i in range(10):
    print(mock.name(), mock.email(), mock.address(), mock.job())