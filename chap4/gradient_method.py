# coding: UTF-8

import numpy as np
import matplotlib.pyplot as plt

step = 100                #�X�e�b�v��
lrate = 0.01              #�w�K��
h = 1e-4

def targetfunc(x):
    return 2*x[0]**2 + x[1]

def gradient(f, x):         #�֐�f�̓_x�ɂ�����O���f�B�G���g
    for i in range(len(x)):
        fdot[i] = (f(x+h) - f(x-h)) / (2*h)

    return fdot

def gradient_decent(f, init_x):
    x = init_x
    for i in range(step):
        grad = gradient(f, x)
        x -= lrate * grad

    return x


init_x = np.array([-3.0, 4.0])
x = gradient_decent(targetfunc, init_x)
print(x)
