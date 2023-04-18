import random

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
    number = random.randint(1000,9999)
    ld = last_digit(number)
    fd = first_digits(number)
    ld1, fd1 = first_last_digits(number)
    print(number, fd, ld,'------', fd1, ld1)
