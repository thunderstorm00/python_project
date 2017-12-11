#sorted()也是一个高阶函数。用sorted()排序的关键在于实现一个映射函数。
print(sorted([36, 5, -12, 9, -21]))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
print(sorted([36, 5, -12, 9, -21], key=abs , reverse=True))
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
from operator import itemgetter

def by_name(t):
    return t[0]
print(sorted(L,key=itemgetter(0)))