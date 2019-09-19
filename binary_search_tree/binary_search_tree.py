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
    def in_order_print(self, node):
        if node.left:
            self.in_order_print(node.left)
        print(node.value)
        if node.right:
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(node)
        
        while queue.len() > 0:
            node = queue.dequeue()
            print(node.value)
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(node)
        
        while stack.len() > 0:
            node = stack.pop()
            print(node.value)
            if node.left:
                stack.push(node.left)
            if node.right:
                stack.push(node.right)


    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(node.value)
        if node.left:
            self.pre_order_dft(node.left)
        if node.right:
            self.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node.left:
            self.post_order_dft(node.left)
        if node.right:
            self.post_order_dft(node.right)
        print(node.value)
