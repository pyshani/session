class Node:
    def __init__(self, val, n):
        self.val = val  
        self.kids = [None] * n

class NTree:
    def __init__(self ,n=2):
        self.root = None
        self.n = n


    def append(self, val):
        if self.root is None:
            self.root = Node(val, self.n)
            return

        deq = [self.root]

        while deq:
            cur = deq.pop(0)

            for i in range(self.n):
                if cur.kids[i] is None:
                    cur.kids[i] = Node(val, self.n)
                    return
                else:
                    deq.append(cur.kids[i])
            
        return

t = NTree(3)
for i in range(9):
    t.append(i)
print(t.root.val, t.root.kids[0].val, t.root.kids[1].val, t.root.kids[2].val)

def check_avl(root):
    check_bin = [True]
    check_avl = True

    def dfs(node, res, st, check_bin):
        if not node:
            return
        if node.kids:
            if len(node.kids) > 2:
                check_bin[0] = False
        
        st.append(node.val)

        if node.kids[0] is None and node.kids[1] is None:
            res.append(len(st))
        if node.kids[0]:
            if not (node.kids[0].val < node.val):
                check_bin[0] = False
            dfs(node.kids[0], res, st, check_bin)
        if node.kids[1]:
            if not (node.kids[1].val > node.val):
                check_bin[0] = False
            dfs(node.kids[1], res, st, check_bin )
        st.pop()
    
    res = []
    st = []
    dfs(root, res, st, check_bin)
    if not (max(res) - min(res) <= 1):
        check_avl = False
    return check_avl and check_bin[0]

t2 = NTree(2)
t2.root = Node(7, 2)

t2.root.kids[0] = Node(4, 2)
t2.root.kids[1] = Node(9, 2)
t2.root.kids[0].kids[0] = Node(2, 3)
t2.root.kids[0].kids[1] = Node(5, 2)
t2.root.kids[1].kids[0] = Node(6, 2)
t2.root.kids[1].kids[1] = Node(10, 2)
# t2.root.kids[1].kids[1].kids[1] = Node(2, 2)
# t2.root.kids[1].kids[1].kids[1].kids[1] = Node(2, 2)
# t2.root.kids[1].kids[1].kids[1].kids[1] = Node(22, 2)
print(check_avl(t2.root))
