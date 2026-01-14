a = [[1,1], [8, 10], [1,2], [15,18]]
def func(a):
    a.sort()
    res = []
    while a:
        b = a.pop(0)
        if a:
            if b[1] >= a[0][0]:
                if a[0][1] >= b[1]:
                    new = [b[0], a[0][1]]
                else:
                    new = [b[0], b[1]]
                a[0] = new
            else:
                res.append(b)
        else:
            res.append(b)
    return res

import numpy as np
import matplotlib.pyplot as plt
import time
import random as r

size = np.linspace(100, 10000, 8)
times = []
for s in size:
    t = 0
    s = round(s)
    arr = []
    for i in range(s):
        a = r.randint(1,100)
        b = r.randint(100,200)
        arr.append([a, b])

    for _ in range(10):
        b = arr[::]
        st = time.perf_counter()
        func(b)
        end = time.perf_counter()
        t += end - st
    times.append(t/10)

arr2 = np.log2(size)
arr2 = list(map(lambda x, y: x*x*y, size, arr2))

arrk = list(map(lambda x, y: x/y, times, arr2))
k = sum(arrk)/len(arrk)
arr2 = list(map(lambda x: x*k,arr2))

plt.plot(size, arr2, "-g", label='n^2log(n) Theoretic')
plt.plot(size, times, "-r", label='Practic')
plt.legend()
plt.grid()
plt.show()