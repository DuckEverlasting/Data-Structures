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
            else:
                if not current.right:
                    current.right = BinarySearchTree(value)
                    return 1
                else:
                    current = current.right
            
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

# DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint: Use a recursive, depth first traversal
    def in_order_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass