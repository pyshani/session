def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    m = len(arr)//2

    l = merge_sort(arr[:m])
    r = merge_sort(arr[m:])

    def merge(l, r):
        res = []
        i = j = 0
        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                res.append(l[i])
                i+=1
            else:
                res.append(r[j])
                j+=1
        
        res.extend(l[i:])
        res.extend(r[j:])
        
        return res

    return merge(l, r)

def quick_sort(arr):

    if len(arr) <= 1:
        return arr
    
    p = arr[len(arr)//2]

    l = [x for x in arr if x < p]
    m = [x for x in arr if x == p]
    r = [x for x in arr if x > p]

    return quick_sort(l) + m + quick_sort(r)


arr = [1, 23, 55, 34, 1, 35, 5,6 , 7,2 ,232,4, 23, 324,234]
print(quick_sort(arr))
print(merge_sort(arr))

import matplotlib.pyplot as plt
import numpy as np
import time
import random as r

size = np.linspace(100,10000, 7)
timesq = []
timesm = []

for s in size:
    s = round(s)
    l = []
    for _ in range(s):
        p = r.randint(100, 1000000)
        l.append(p)
    t = 0

    for _ in range(10):
        k = l.copy()
        st = time.perf_counter()
        quick_sort(k)
        end = time.perf_counter()
        t += end - st
    timesq.append(t/10)
    
    t = 0
    for _ in range(10):
        k = l.copy()
        st = time.perf_counter()
        merge_sort(k)
        end = time.perf_counter()
        t += end - st
    timesm.append(t/10)

theor = np.log2(size)
theor = list(map(lambda x, y: x*y, size,theor))

arrk = list(map(lambda x, y: x/y, timesm, theor))
k = sum(arrk)/len(arrk)
print(k)

theor = list(map(lambda x: x*k, theor))

plt.plot(size, theor, '-g', label="Theor nlog(n)")
plt.plot(size, timesq, '-r', label="Practic quick_sort")
plt.plot(size, timesm, '-y', label="Practic merge_sort")
plt.grid()
plt.legend()
plt.show()

