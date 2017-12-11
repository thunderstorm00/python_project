# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 21:37:38 2017

@author: thunderstorm
"""

import numpy as np 
import tensorflow as tf
import matplotlib.pyplot as plt

#定义训练数据
x_data = np.linspace(-2, 2, num = 200).reshape([200, 1])
noise = np.random.normal(0, 0.2, x_data.shape)
y_data = np.square(x_data) + noise


#定义占位符号
x = tf.placeholder(tf.float32, x_data.shape)
y = tf.placeholder(tf.float32, x_data.shape)

#创建第一层
w1 = tf.Variable(tf.random_normal([1, 10]))
b1 = tf.Variable(tf.zeros([1, 10]))
w1x_plus_b1 = tf.matmul(x, w1) + b1
y1 = tf.nn.tanh(w1x_plus_b1)

#创建第二层： 输出层
w2 = tf.Variable(tf.random_normal([10, 1]))
b2 = tf.Variable(tf.zeros([1, 1]))
w2x_plus_b2 = tf.matmul(y1, w2) + b2
y2 = tf.nn.tanh(w2x_plus_b2)

#定义损失函数
loss = tf.reduce_mean(tf.square(y - y2))

#定义optimizer
optimizer = tf.train.GradientDescentOptimizer(0.2)
train = optimizer.minimize(loss)

#训练
with tf.Session() as sess:
    #初始化变量
    sess.run(tf.global_variables_initializer())
    for _ in range(2000):
        sess.run(train, feed_dict = {x:x_data, y:y_data})
        #获取得预测值
        prediction_value = sess.run(y2,feed_dict={x:x_data})
        if _%200 == 0:
            #画图
            plt.figure()
            plt.scatter(x_data,y_data)
            plt.plot(x_data,prediction_value,'r-',lw=5)
            plt.show()
        
