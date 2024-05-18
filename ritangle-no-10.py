step = 0.01
last = 11
from math import floor, ceil
import numpy as np
l = []
for i in np.arange(1.42, 3, step):
    exp = ceil(floor(ceil(floor(i)+i**2)+i**3)+i**4)
    if not (exp in l):
        l.append(exp)
l2 = []
for i in range(11, l[-1]):
    if not (i in l):
        l2.append(i)

print(l2)