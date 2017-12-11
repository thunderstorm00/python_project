# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 11:48:21 2017

@author: thunderstorm
"""

import tensorflow as tf
#Variable 和 tensor 不一样，Variable存在于单个的session.run调用的上下文之外
def add_layer(inputs, in_size, out_size, activation_function = None):
     Weights = tf.Variable(tf.random_normal(in_size, out_size),activation_dunction = None)
     biases = tf.Variable(tf.zeros(1, out_size)+ 0.1)
     Wx_plus_b = tf.matmul(inputs, Weights)+biases
     if activation_function is None:
         outputs = Wx_plus_b
     else:
         outputs = activation_function(Wx_plus_b)
    return outputs




