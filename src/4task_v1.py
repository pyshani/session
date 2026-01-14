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

def checkbst(node, c, d):
    if node is None:
        return True
    
    if not(c < node.val < d):
        return False
    
    if node.right:
        if not (node.right.val > node.val):
            return False
        
    if node.left:
        if not (node.left.val < node.val):
            return False

    return checkbst(node.left, c, d) and checkbst(node.right, c, d)

def checkmaxminheap(node, a, b):
    if node is None:
        return True

    root = node

    result = []
    queue = [node]

    min_ch = True
    max_ch = True
    check_heap = True
    checkheight = True
    cnt_unfull_lev = 0

    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.pop(0)

            if node:
                current_level.append(node.val)
            else:
                current_level.append(None)
                continue

            if node.left:
                if max_ch:
                    if not (node.left.val < node.val):
                        max_ch = False
                if min_ch:
                    if not (node.left.val > node.val):
                        min_ch = False
                queue.append(node.left)
            else:
                queue.append(None)
            if node.right:
                if max_ch:
                    if not (node.right.val < node.val):
                        max_ch = False
                if min_ch:
                    if not (node.right.val > node.val):
                        min_ch = False
                queue.append(node.right)
            else:
                queue.append(None)
        if not all(x is None for x in current_level):
            result.append(current_level)
            if None in current_level:
                cnt_unfull_lev+=1
    
    if not (cnt_unfull_lev <= 1):
        check_heap = False
    
    if not (a < len(result) < b):
        checkheight = False
    
    print(result)
    
    # print(checkheight)
    # print(check_heap)
    # print(min_ch)
    # print(max_ch)
    
    return checkheight and check_heap and (min_ch or max_ch)


tree = BTree()
for i in range(10):
    tree.append(i)

tree2 = BTree()
tree2.append(10)
tree2.append(6)
tree2.append(15)
tree2.append(3)
tree2.append(7)
tree2.append(11)
tree2.append(18)

print(checkmaxminheap(tree.root, 2, 10))
print(checkbst(tree2.root, 2, 20))