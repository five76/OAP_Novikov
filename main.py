food = ['Шашлык','Огурцы','Молоко','Творог','Яблоки','Яйца','Шоколад','Томаты']
price = [1000,100,60,500,150,100,70,130]
count = [2.5,3,2,1.5,2.5,2,3,3]
print(food[0])
print(price[0])
# Неправильный код
print(food[0],price[0])
print(food[1],price[1])
print(food[2],price[2])
print(food[3],price[3])
print(food[4],price[4])
print(food[5],price[5])
# Более-менее правильный код
print('*'*80)
for index in range(0,7):
    print(food[index],price[index])
    # Более-менее правильный код
print('*' * 80)
for index in range(0, 7):
    print(food[index], price[index])
# Еще Более правильный код
print('*'*80)
for index in range(0,len(food)): # range(0,100) тоже самое, что  range(100)
    print(food[index],price[index])
# и Еще Более правильный код
print('-'*26)
for index in range(0,len(food)): # range(0,100) тоже самое, что  range(100)
    print("|{0:15} | {1:5} |".format(food[index],price[index]))
print('-'*26)
# Подсчет суммы покупки
print('-'*26)
s = 0
for index in range(0,len(food)): # range(0,100) тоже самое, что  range(100)
    s1 = price[index] * count[index]
    print("|{0:15} | {1:5} |".format(food[index],s1))
    s+= s1

print(f'Итого {s} рублей')
