# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 17:04:18 2017

@author: thunderstorm
"""

# =============================================================================
# 直方图：plt.hist(data, number,normed = 1, histtype = 'stepfilled', facecolor = 'b', alpha = 0.75)
# 示例：采用numpy正态分布生成数据array
# =============================================================================
import matplotlib.pyplot as plt
import numpy as np 

np.random.seed(0)
mu , sigma = 100, 20
a = np.random.normal(mu, sigma, size = 100)
plt.hist(a, 20,normed = 1, histtype = 'stepfilled', facecolor = 'b', alpha = 0.75)
plt.title("hist_ogram")
plt.show()
