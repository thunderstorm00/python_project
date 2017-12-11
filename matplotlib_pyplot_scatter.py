# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 21:46:14 2017

@author: thunderstorm
"""

import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot(10* np.random.randn(100), 10 * np.random.randn(100), 'o')
ax.set_title('simple_Scatter')
plt.show()