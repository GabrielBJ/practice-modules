

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

def transform_1(x, y):
    return x, 0.16*y

def transform_2(x, y):
    return 0.85*x + 0.04*y, -0.04*x + 0.85*y + 1.6

def transform_3(x, y):
    return 0.2*x - 0.26*y, 0.23*x + 0.22*y + 1.6

def transform_4(x, y):
    return -0.15*x + 0.28*y, 0.26*x + 0.24*y + 0.44

func_barnsley = [transform_1, transform_2, transform_3, transform_4]

points = 100000
x, y = 0, 0
x_list, y_list = [], []

for _ in range(points):
    transformation = np.random.choice(func_barnsley, p=[0.01, 0.85,
                                                        0.07, 0.07])

    x, y = transformation(x, y)
    x_list.append(x)
    y_list.append(y)

plt.figure(figsize=(10, 8))
plt.scatter(x_list, y_list, s=0.2, edgecolor='green', color='green')
plt.show()
