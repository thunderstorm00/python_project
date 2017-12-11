# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt
import numpy as np
import requests

#plt.subplot(3,2,4)
#plt.plot([3,1,4,5,2], [3,1,4,5,2])
#plt.ylabel("grade")
#plt.axis([-1,10,0,6])
##plt.savefig('test', dpi=600)
#plt.show()
try:
    html = requests.get('https://www.baidu.com/')
    html.raise_for_status()
    html.encoding = html.apparent_encoding;
    file = open('D://baiduhtml.html', 'w', encoding='utf-8')
    file.write(html.text)
    file.close()
    print(html.text)
except:
    print('error...')
        

def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)

a = np.arange(0.0, 5.0, 0.02)

plt.subplot(211)
plt.plot(a, f(a))
plt.subplot(212)
plt.plot(a, f(a),a, np.cos(2*np.pi*a),a, np.sin(2*np.pi*a), 'r--')
plt.show()

