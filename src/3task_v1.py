import numpy as np
import matplotlib.pyplot as plt
import time

class Node:
    def __init__(self, val):
        self.val = val  
        self.left = None
        self.right = None

class BTree:
    def __init__(self):
        self.root = None

    def append(self, val):
        if self.root is None:
            self.root = Node(val)
            return

        deq = [self.root]

        while deq:
            cur = deq.pop(0)

            if cur.left is None:
                cur.left = Node(val)
                return
            else:
                deq.append(cur.left)
            
            if cur.right is None:
                cur.right = Node(val)
                return
            else:
                deq.append(cur.right)
        return

def check(root):
    if root is None:
        return True
    
    def mir(left, right):
        
        if left is None and right is None:
            return True
        if left is  None or right is None:
            return False
        
        return (left.val == right.val and mir(left.left, right.right) and mir(left.right, right.left))

    return mir(root.left, root.right)
    

tree = BTree()

for i in range(10):
    tree.append(i)

tree2 = BTree()
tree2.append(1)
tree2.append(2)
tree2.append(2)
tree2.append(3)
tree2.append(3)
tree2.append(3)
tree2.append(3)


print(check(tree.root))
print(check(tree2.root))

arr = np.linspace(1, 100, 5)
arr2 = np.linspace(1, 100, 5)

times2 = []
for s in arr2:
    s = round(s)
    t = 0
    tree = BTree()

    l = 1
    for i in range(round(np.log2(s))):
        for _ in range(2**i):
            tree.append(l)
        l+=1

    for _ in range(10):
        start = time.perf_counter()
        check(tree.root)
        end = time.perf_counter()
        t += end - start
    times2.append(t/10)

times = []
for s in arr2:
    s = round(s)
    t = 0
    tree = BTree()
    for i in range(s):
        tree.append(i)

    for _ in range(10):
        start = time.perf_counter()
        check(tree.root)
        end = time.perf_counter()
        t += end - start
    times.append(t/10)
k = 1
karr = list(map(lambda x, y: x/y, times, arr2))
k = sum(karr)/len(karr)

arr3 = list(map(lambda x: x*k, arr))

arre = [0] * len(arr)

plt.plot(arr, arr3, '-y', label="O(n)")
plt.plot(arr2, times, '-g', label="best")
plt.plot(arr2, times2, '-r', label="worst")
plt.plot(arr, arre, '-y', label="O(1)")
plt.legend()
plt.grid()
plt.show()