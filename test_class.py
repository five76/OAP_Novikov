import random

class Person:
    def __init__(self,name,job,pay):
        self.name = name
        self.job = job
        self.pay = pay

    def display(self):
        print(self.data)

class I1(C1):
    def display(self):
        print(f'Это данные {self.data}')


E1 = C1()
E2 = I1()
E1.set_data('Class C1')
E2.set_data('Class I1')
E1.display()
E2.display()
E2.count = 5
E2.set_data(E2.count)
E2.display()
E1.set_data(E2.count)
E1.display()
