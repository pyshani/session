class NodeU:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedListMod:
    def __init__(self):
        self.head = None
        self.min = None
        self.max = None
    
    def append(self, val):
        if self.head is None:
            self.head = NodeU(val)
            self.min = val
            self.max = val
        else:
            node = NodeU(val)
            node.next = self.head
            self.head = node
            if val < self.min: self.min = val
            if val > self.max: self.max = val
    
    def check_max_min(self, val):
        if val == self.min or val == self.max:
            cur = self.head
            self.min = cur.val
            self.max = cur.val
            while cur:
                if cur.val < self.min:
                    self.min = cur.val
                if cur.val > self.max:
                    self.max = cur.val
                cur = cur.next
        
    def delete(self, val):
        if self.head.val == val:
            self.head = self.head.next
        else:
            cur = self.head
            while cur:
                if cur.val == val:
                    if cur.next is None:
                        prev.next = None
                    else:
                        prev.next = cur.next
                    return
                prev = cur
                cur = cur.next

        self.check_max_min(val)

    def get_max(self):
        return self.max
    
    def get_min(self):
        return self.min

class LinkedList:
    def __init__(self):
        self.head = None

    
    def append(self, val):
        if self.head is None:
            self.head = NodeU(val)
        else:
            node = NodeU(val)
            node.next = self.head
            self.head = node
    
        
    def delete(self, val):
        if self.head.val == val:
            self.head = self.head.next
        else:
            cur = self.head
            while cur:
                if cur.val == val:
                    if cur.next is None:
                        prev.next = None
                    else:
                        prev.next = cur.next
                    return
                prev = cur
                cur = cur.next

class NodeD:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class DoublyLinkedListMod:
    def __init__(self):
        self.head = None
        self.tail = None
        self.min_val = None
        self.max_val = None

    def append(self, val):
        node = NodeD(val)
        if not self.head:
            self.head = node
            self.tail = node
            self.min_val = val
            self.max_val = val
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
            
            if val < self.min_val:
                self.min_val = val
            if val > self.max_val:
                self.max_val = val

    def _recalculate_min_max(self):
            
        cur = self.head
        self.min_val = cur.val
        self.max_val = cur.val
        
        while cur:
            if cur.val < self.min_val:
                self.min_val = cur.val
            if cur.val > self.max_val:
                self.max_val = cur.val
            cur = cur.next

    def delete(self, val):
        if not self.head:
            return

        current = self.head
        found = False
        
        while current:
            if current.val == val:
                found = True
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                break
            current = current.next

        if found:
            if val == self.min_val or val == self.max_val:
                self._recalculate_min_max()

    def get_min(self):
        return self.min_val

    def get_max(self):
        return self.max_val

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, val):
        node = NodeD(val)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

    def delete(self, val):
        if not self.head:
            return

        cur = self.head
        while cur:
            if cur.val == val:
                if cur.prev:
                    cur.prev.next = cur.next
                else:
                    self.head = cur.next

                if cur.next:
                    cur.next.prev = cur.prev
                else:
                    self.tail = cur.prev
                return

            cur = cur.next

import numpy as np
import matplotlib.pyplot as plt
import time


l1 = LinkedList()
l1m = LinkedListMod()
l2 = DoublyLinkedList()
l2m = DoublyLinkedList()


