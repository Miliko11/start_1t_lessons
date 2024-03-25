'''
list1 = ['a', 'b', 'c'] # a = 0, b = 1, c = 2 и т.д.
print(list1)
print(list1[0])
print(list1[1])
print(list1[2])
'''

list2 = [11, 22, 33, 44, 55]
print(list2)
print(list2[1])
print(list2[4]) # одинаковы
print(list2[-1]) # одинаковы
list2.append(66)
print(list2)
print(list2[5])
list2.insert(2, 0) # лучше использовать append чем эту
print(list2)
list2[0] = 99
print(list2)
del list2[0]
print(list2)
list2.remove(55)
print(list2)

lsit_empty = []
list_empty = list()

