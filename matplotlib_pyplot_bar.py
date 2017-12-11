# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 20:34:26 2017

@author: thunderstorm
"""

# =============================================================================
# 极坐标图
# =============================================================================

import numpy as np
import matplotlib.pyplot as plt

N = 20
#返回0-2pi之间的N个数
theta = np.linspace(0.0, 2* np.pi, N , endpoint = False)
#each integer specifier the size of one dimention
#返回数列包含N个浮点小数0-10
radii = 10 * np.random.rand(N)
width = np.pi / 4 * np.random.rand(N)

#面向对象的方法绘图
ax = plt.subplot(111, projection = 'polar')
bars = ax.bar(theta, radii, width = width, bottom = 0.0)

for r, bar in zip (radii, bars):
    bar.set_facecolor(plt.cm.viridis(r/10.))
    bar.set_alpha(0.5)
plt.show()
 