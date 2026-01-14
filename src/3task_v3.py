import numpy as np
import matplotlib.pyplot as plt
import time 
import math

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
    
    def append(self, val):
        if self.root is None:
            self.root = Node(val)
            return
        que = [self.root]
        while que:
            cur = que.pop(0)

            if cur.left is None:
                cur.left = Node(val)
                return
            else:
                que.append(cur.left)

            if cur.right is None:
                cur.right = Node(val)
                return
            else:
                que.append(cur.right)

def findway(root):
    def dfs(node, res, st):
        if not node:
            return
        
        st.append(node.val)

        if not node.left and not node.right:
            if sum(res[max]) < sum(st):
                res[max] = st[::]   
            if sum(res[min]) > sum(st):
                res[min] = st[::]
        if node.left:
            dfs(node.left, res, st)
        if node.right:
            dfs(node.right, res, st)
        st.pop()
    
    res = {max: [-math.inf], min: [math.inf]}
    st = []
    dfs(root, res, st)
    return res[min], res[max]

def checkfunc():
    t = Tree()

    for i in range(10):
        t.append(i)

    print(*findway(t.root))

def graphs():

    sizes = np.linspace(1,1000, 6)

    times = []
    for s in sizes:
        s = round(s)
        a = 10
        b = 100
        t = 0
        tree = Tree()    
        for i in range(s):
            tree.append(s)

        for _ in range(10):
            st = time.perf_counter()
            findway(tree.root)
            en = time.perf_counter()
            t+= en - st
        times.append(t/10)
    
    arrk = list(map(lambda x, y: x/y , times, sizes))
    k = sum(arrk)/len(arrk)
    timesy = list(map(lambda x: x*k, sizes))

    plt.plot(sizes, times, '-r', label="Practic O(n)")
    plt.plot(sizes, timesy, '-b', label="Theoretic O(n)")

    plt.legend()
    plt.grid()
    plt.show()

# checkfunc()
graphs()