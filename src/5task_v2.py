class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTableCh:
    def __init__(self, size=5):
        self.size = size
        self.table = [None] * size
    
    def _hash(self, key):
        return sum(ord(c) for c in str(key)) % self.size
    
    def put(self, key, value):
        index = self._hash(key)
        
        if self.table[index] is None:
            self.table[index] = Node(key, value)
            return
        
        current = self.table[index]
        while current:
            if current.key == key:
                current.value = value
                return
            if current.next is None:
                break
            current = current.next
        
        current.next = Node(key, value)
    
    def get(self, key):
        index = self._hash(key)
        current = self.table[index]
        
        while current:
            if current.key == key:
                return current.value
            current = current.next
        
        raise KeyError(f"Key '{key}' not found")
    
    def __str__(self):
        result = []
        for i in range(self.size):
            chain = []
            current = self.table[i]
            while current:
                chain.append(f"{current.key}:{current.value}")
                current = current.next
            result.append(f"[{i}]: {' -> '.join(chain) if chain else 'empty'}")
        return "\n".join(result)
    
class HashTableOp:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size
    
    def _hash(self, key):
        return hash(key) % self.size
    
    def put(self, key, value):
        index = self._hash(key)
        
        for i in range(self.size):
            idx = (index + i) % self.size
            if self.table[idx] is None:
                self.table[idx] = (key, value)
                return
            elif self.table[idx][0] == key:
                self.table[idx] = (key, value)
                return
        
        raise Exception("Table is full")
    
    def get(self, key):
        index = self._hash(key)
        
        for i in range(self.size):
            idx = (index + i) % self.size
            if self.table[idx] is None:
                break
            if self.table[idx][0] == key:
                return self.table[idx][1]
        
        raise KeyError(f"Key '{key}' not found")
    
    def remove(self, key):
        index = self._hash(key)
        
        for i in range(self.size):
            idx = (index + i) % self.size
            if self.table[idx] is None:
                return False
            if self.table[idx][0] == key:
                self.table[idx] = None
                
                # Перемещаем последующие элементы
                next_idx = (idx + 1) % self.size
                while self.table[next_idx] is not None:
                    item_key, item_value = self.table[next_idx]
                    self.table[next_idx] = None
                    self.put(item_key, item_value)
                    next_idx = (next_idx + 1) % self.size
                
                return True
        
        return False
    
    def __str__(self):
        result = []
        for i, item in enumerate(self.table):
            if item is None:
                result.append(f"[{i}]: empty")
            else:
                result.append(f"[{i}]: {item[0]}:{item[1]}")
        return "\n".join(result)



ht = HashTableCh(5)

ht.put('cat', 100)
ht.put('dog', 200)
ht.put('act', 300)
print(ht)
print(ht.get("act"))

    
