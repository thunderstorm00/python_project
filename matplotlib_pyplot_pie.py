# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 16:56:41 2017

@author: thunderstorm
"""

import matplotlib.pyplot as plt

labels = ['1', '2', '3', '4']
explode = [0.1, 0.1, 0.1, 0.1]
sizes = [15, 25, 35, 25]
plt.axis('equal')
plt.pie(sizes, explode = explode, labels = labels, autopct = '%1.1f%%',shadow = False, startangle = 90)