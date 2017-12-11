# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 20:45:58 2017

@author: thunderstorm
"""

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

#载入数据集
mnist = input_data.read_data_sets("MINST_data", one_hot = True)

#每个批次的大小
batch_size = 500

#计算一共有多少个批次
n_batch = mnist.train.num_examples // batch_size
print("n_batch: " + str(n_batch))

#定义两个占位符、
x = tf.placeholder(tf.float32,[None, 784])
y = tf.placeholder(tf.float32,[None, 10])

#创建一层简单的神经网络
w1 = tf.Variable(tf.zeros([784,20]))
b1 = tf.Variable(tf.zeros([1, 20]))
y1 = tf.matmul(x, w1) + b1

#创建第二层神经网络
w2 = tf.Variable(tf.random_normal([20,20]))
b2 = tf.Variable(tf.zeros([1, 20]))
y2 = tf.matmul(y1, w2)+ b2


#创建第三层神经网络
w3 = tf.Variable(tf.random_normal([20, 10]))
b3 = tf.Variable(tf.zeros([1, 10]))
y3 = tf.matmul(y2, w3) + b3
prediction = tf.nn.softmax(y3)

#二次代价函数
loss = tf.reduce_mean(tf.square(prediction - y))

#训练，梯度下降法
train = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

#初始化变量
init = tf.global_variables_initializer()

#结果存放在一个布尔型列表中
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(prediction, 1))

#求准确率
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

#开始训练
with tf.Session() as sess:
    sess.run(init)
    for epoch in range(50):
        for batch in range(batch_size):
            batch_xs, batch_ys = mnist.train.next_batch(batch_size)
            sess.run(train, feed_dict = {x : batch_xs, y : batch_ys})
        if epoch%5 == 0:
            acc = sess.run(accuracy,feed_dict={x:mnist.test.images,y:mnist.test.labels})
            print("Iter " + str(epoch) + ",Testing Accuracy " + str(acc))










