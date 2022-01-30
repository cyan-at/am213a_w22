#!/usr/bin/env python3

'''
USAGE: ./hw1q12.py
'''

import numpy as np
np.set_printoptions(precision=3)
np.set_printoptions(suppress=True)
np.set_printoptions(formatter={'float': '{: 0.4f}'.format})

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def f(x):
    return (x-2) ** 9

def g(x):
    return x**9 - 18 * x ** 8 + 144 * x ** 7 - 672 * x ** 6 + 2016 * x ** 5 - 4032 * x ** 4 + 5376 * x ** 3 - 4608 * x ** 2 + 2304 * x - 512

# a
x = [1.92]
while (x[-1] < 2.080):
    x.append(x[-1] + 0.001)

fx = [f(xi) for xi in x]

gx = [g(xi) for xi in x]

plt.plot(x, fx, c = 'r', label='f(x)')
plt.plot(x, gx, c = 'b', label='g(x)')

plt.title('HW1 Q12 (a),(b)')
plt.legend()

plt.show()

# part c:
'''
It is clear that small perturbations in the polynomial expression x value yield non-trivial perturbations in the output g(x)
much more so than the original function f(x)

As the book covers, polynomial rootfinding is ill-conditioned, where small changes in coefficients (or small input perturbations)
can lead to large change in the roots

In other words, the small discrete inputs to g(x) resembling small changes in the coefficients of the polynomial
represent large changes in the roots of the polynomial aka the underlying mathematical function being represented

So when doing discrete calculations of a function it is always better to use an expression of a function
That is well-conditioned (f(x) = (x-2)**9) and avoid one that is not (g(x))
'''