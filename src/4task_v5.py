def three_sum(nums):
    nums.sort()
    result = []
    n = len(nums)
    
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
            
        left, right = i + 1, n - 1    
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                    
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    
    return result

arr = [-1, 0, 1, 2, -1, -4]

print(three_sum(arr))

import matplotlib.pyplot as plt
import numpy as np
import time

size = np.linspace(100, 1000, 6)
arr2 = list(map(lambda x: x*x, size))
times = []
for s in size:
    t = 0
    s = round(s)
    l = []
    for i in range(s):
        l.append(i)
    for _ in range(10):
        st = time.perf_counter()
        three_sum(l)
        end = time.perf_counter()
        t += end - st
    times.append(t/10)

arrk = list(map(lambda x, y: x/y, times, arr2))
k = sum(arrk)/len(arrk)
arr2 = list(map(lambda x: x*k, arr2))

plt.plot(size, times, '-b', label="Practic O(n^2)")
plt.plot(size, arr2, '-r', label="Theoretic O(n^2)")
plt.grid()
plt.legend()
plt.show()