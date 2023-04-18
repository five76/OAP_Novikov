def unique(lst):
    lst_uniq = []
    for elem in lst:
        if elem not in lst_uniq:
            lst_uniq.append(elem)
    return lst_uniq


mylist = [1, 1, 2, 1, 3, 2, 3]
print(mylist)
print(unique(mylist))