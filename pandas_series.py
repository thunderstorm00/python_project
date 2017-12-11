# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 21:51:28 2017

@author: thunderstorm
"""

# =============================================================================
# numpy, 基础的数据类型，数据的结构表达维度
# pandas, series,dataframs,扩展数据类型, 关注数据的应用表达
#
#series是由一组数据和与之相关的索引组成
# =============================================================================
import pandas as pd
import numpy as np

d = pd.Series(range(20))
print(d)
d = d.cumsum()
print(d)

#从标量值创建
s = pd .Series(25, index = ['a','b','c'])
print(s)
#从字典类型创建
s_dict = {'a':1, 'b':2, 'c':3}
print(pd.Series(s_dict))
print(pd.Series(s_dict, index = ['c', 'a', 'b', 'd']))
#从ndarray类型创建
n = pd.Series(np.arange(5), np.arange(9, 4, -1))
print(n)

#基本操作
b = pd.Series([9, 8, 7, 6], index = ['a', 'b', 'c', 'd'])
print(b)
print(b.index)
print(b.values)
print(b['b'])
print(b[1])
print(9 in b)
print(b.get('a'))
print(b[0:4:2])

print(pd.Series(s_dict, index = ['c', 'a', 'b', 'd']) + b)














