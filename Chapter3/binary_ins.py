# бинарный поиск дерева с сортировкой по возростанию


# from random import random
#
# N = 10
# array = []
# # заполнение массива
# for i in range(N):
#     array.append(int(random() * 100))
#
# # сортировка массива
# array.sort()
#
# print(array)
#
# # число, которое требуется найти
# number = int(input(": "))
#
# # нижний (начальный) индекс
# low = 0
# # верхний (конечный) индекс
# high = N - 1
# # как только нижний индекс станет больше на 1 верхнего
# # или верхний на 1 меньше нижнего цикл остановится
# while low <= high:
#     # находится индекс середины массива или отрезка массива
#     mid = (low + high) // 2
#     # Если искомое число меньше числа с индексом середины,
#     if number < array[mid]:
#         # то верхняя граница сдвигается к середине (но на 1 до нее,
#         # т. к. середина была уже проверена)
#         high = mid - 1
#     # Если искомое число больше числа с индексом середины,
#     elif number > array[mid]:
#         # то нижняя граница сдвигается за середину
#         low = mid + 1
#     # Все остальные случаи возникают, когда искомое число
#     # равно числу с индексом mid, т.е. оно есть в массиве и найдено
#     else:
#         print("ID =", mid)
#         # прерывание цикла
#         break
# # ветка else сработает, если не было break и условие при while стало ложным,
# # т.е. тогда, когда нижняя граница станет больше верхней. Это значит, что
# # в массиве нет искомого числа.
# else:
#     print("No the number")







class BTree(object):
    def __init__(self, data):
        self.data = data
        self.rChild = None
        self.lChild = None

    def __str__(self):
        return (self.lChild.__str__() + '<-' if self.lChild != None else '') + \
               self.data.__str__() + ('->' + self.rChild.__str__()
                                      if self.rChild != None else '')

    def insert(self, btree):
        if self.data > btree.data: #insert left
            if self.lChild == None:
                self.lChild = btree
            else:
                self.lChild.insert(btree)
        else: #insert right
            if self.rChild == None:
                self.rChild = btree
            else:
                self.rChild.insert(btree)

# root = Node(50)
# root = root.addNode(30)
# root = root.addNode(20)
# root = root.addNode(40)
# root = root.addNode(70)
# root = root.addNode(60)
# root = root.addNode(80)

def main():
    btreeRoot = BTree(50)
    print('inserted %s:' %50, btreeRoot)

    btreeRoot.insert(BTree(30))
    print('inserted %s:' %30, btreeRoot)

    btreeRoot.insert(BTree(20))
    print('inserted %s:' %20, btreeRoot)

    btreeRoot.insert(BTree(40))
    print('inserted %s:' %40, btreeRoot)

    btreeRoot.insert(BTree(70))
    print('inserted %s:' %70, btreeRoot)

    btreeRoot.insert(BTree(60))
    print('inserted %s:' %60, btreeRoot)

    btreeRoot.insert(BTree(80))
    print('inserted %s:' %80, btreeRoot)
main()









# Вариант 1. Использование встроенного типа данных complex:
#
# a = input()
# b = input()
# a = complex(a)
# b = complex(b)
# suma = a + b
# mult = a * b
# print(suma)
# print(mult)

# Вариант 2. Определение собственного класса и перегрузка операторов:

# Вариант 3. Использование словарей:
#
# a = {'x':0, 'y':0}
# b = {'x':0, 'y':0}
# a['x'] = float(input())
# a['y'] = float(input())
# b['x'] = float(input())
# b['y'] = float(input())
# suma = {}
# mult = {}
# suma['x'] = a['x'] + b['x']
# suma['y'] = a['y'] + b['y']
# mult['x'] = a['x'] * b['x'] - a['y'] * b['y']
# mult['y'] = a['y'] * b['x'] + a['x'] * b['y']
# print('Сумма:   %.2f+%.2fj' % (suma['x'], suma['y']))
# print('Произв.: %.2f+%.2fj' % (mult['x'], mult['y']))

