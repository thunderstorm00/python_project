# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 17:39:29 2017


@author: thunderstorm
"""

import tensorflow as tf
import numpy as np

x_data = np.random.rand(100)
y_data = x_data* 0.1 + 0.2

#构造一个线性模型
b = tf.Variable(0.)
w = tf.Variable(0.)
y = w* x_data + b

#定义损失函数
loss = tf.reduce_mean(tf.square(y_data-y))
#定义一个梯度下降法来进行训练的优化器
train = tf.train.GradientDescentOptimizer(0.01).minimize(loss)

#开始训练
with tf.Session() as sess:
    #初始化变量
    sess.run(tf.global_variables_initializer())
    for _ in range(1000):
        sess.run(train)
        if _%100 == 0:
            print(_, sess.run([w, b]))