# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 17:03:15 2017

@author: thunderstorm
"""

import tensorflow as tf

a = tf.Variable([[1,2]], name = 'counter')
b = tf.constant([[3,4]])

init = tf.global_variables_initializer()
c = tf.assign(a, b+a)

with tf.Session() as sess:
    sess.run(init)
    print(sess.run(tf.subtract(a, b)))
    print(sess.run(tf.add(a, b)))
    for _ in range(5):
        print(sess.run(c))


