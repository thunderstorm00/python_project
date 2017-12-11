# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 13:56:47 2017

@author: thunderstorm
"""

# =============================================================================
# DataFrame是一个表格行数据类型，每列值类型可以不同
# 既有行索引，也有列索引
# 常表达二位数据，可表达多维数据
# =============================================================================

import pandas as pd
import numpy as np

#由ndarray创建
d = pd.DataFrame(np.arange(10).reshape(2, 5))
print(d)
#由字典创建
dt = {'one':pd.Series([1,2,3],index = ['a','b', 'c']),
      'two': pd.Series([9,8,7,6],['a','b','c','d'])}
d = pd.DataFrame(dt)
print(d)