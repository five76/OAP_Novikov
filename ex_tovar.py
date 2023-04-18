from pprint import pprint
with open('tovar.txt', encoding='utf8') as f:
    tovar_input = []
    for line in f:
        tovar_input.append(line[:-1])
pprint(tovar_input)
print('-'*80)
tovar_lst = []
for t in tovar_input:
    tovar_lst.append(t.split('\t'))
pprint(tovar_lst)

quest = 'свежая рыба'
sum_total = 0
country = set()
for i in tovar_lst:
    if quest in i[0]:
        sum_total += float(i[1])
        country.add(i[2])
print(f'Товара "{quest}" экспортировано \
{sum_total} в {country}')
