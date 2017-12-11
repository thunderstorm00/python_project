# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 15:13:03 2017

@author: thunderstorm
"""

import matplotlib.pyplot as plt 
import numpy as np

#array = np.arange(10);
#plt.plot(array, array*1, 'r*-',array, array*0.5, 'b-.', array, array*2, 'x')

a = np.arange(0, 5, 0.02)
plt.subplot2grid((3,3), (0, 0), colspan = 3)
plt.subplot2grid((3,3), (0, 1), colspan = 2)
plt.plot(a, np.cos(2* np.pi * a), 'r-.')
plt.xlabel('横轴：时间', fontproperties = 'fangsong',fontsize= '20')
plt.ylabel('纵轴：振幅', fontproperties = 'fangsong',fontsize = '20')
plt.title('图标如下：', fontproperties = 'fangsong',fontsize = '20')
plt.text(2,1,'$y = cos(2\pi x)$' , fontsize = '15')
plt.annotate('this  a yu xuan curve', xy = (1, 1), xytext = (2, 1.5), arrowprops= dict(facecolor = 'black'))
plt.axis([-1, 6,-1, 2])
plt.grid(b = True)