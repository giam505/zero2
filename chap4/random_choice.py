# coding: UTF-8               #���{����g�p����ۂ�1,2�s�ڂɂ���

import numpy as np

max = 10
n = 5

x = np.random.choice(max, n)      #create a list that has n integars chosen randomly from [0, max-1] with duplication
print(x)

y = np.random.choice(max,n,replace=False)      #without duplication
print(y)

alist = ["a", "b", "c"]
z = np.random.choice(alist, 2)
print(z)

weight0 = [1,4,6,16,25,36,49,64,81,100]       #�w�肵���m���Œ��o�i�d�݂͐��K������K�v������j
weight1 = weight0 / np.sum(weight0)
print(weight1)
w = np.random.choice(max, n, p=weight1)
print(w)
