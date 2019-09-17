from dll_queue import Queue
from dll_stack import Stack

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        current = self
        while current:
            if value < current.value:
                if not current.left:
                    current.left = BinarySearchTree(value)
                    return 1
                else:
                    current = current.left
            elif value > current.value:
                if not current.right:
                    current.right = BinarySearchTree(value)
                    return 1
                else:
                    current = current.right
            else:
                return None
            

    def contains(self, target):
        current = self
        while current:
            if target == current.value:
                return True
            elif target < current.value:
                if not current.left:
                    return False
                else:
                    current = current.left
            elif target > current.value:
                if not current.right:
                    return False
                else:
                    current = current.right

    def get_max(self):
        current = self
        while current:
            if current.right:
                current = current.right
            else:
                return current.value

    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

def find_middle(linked_list):
    values = []
    length = 0
    if not linked_list.value:
        return None
    current = linked_list.value
    while current:
        values.append(current.value)
        current = current.next
        length += 1
    
    return values[length // 2]

def reverse(linked_list):
    current = linked_list
    prev = None
    next = current.next
    while current:
        next = current.next 
        current.next = prev
        current = next
        \

  