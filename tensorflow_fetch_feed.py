# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 17:20:58 2017

@author: thunderstorm
"""
import tensorflow as tf
#Fetch
a = tf.constant(1.)
b = tf.constant(2.)
op1 = tf.subtract(a, b)
op2 = tf.add(a, b)

with tf.Session() as sess:
    print(sess.run([op1, op2]))
 
    
#Feed
c = tf.placeholder(tf.float32)
d = tf.placeholder(tf.float32)

with tf.Session() as sess:
    #feed数据以字典形式传入
    print(sess.run(tf.multiply(c, d), feed_dict = {c:1, d:2}))