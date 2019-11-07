lst = [1, 2, 3, 4, 5]

e1 = lst[-1]
for i, e2 in enumerate(lst):
    lst[i], e1 = e1, e2

print(lst)