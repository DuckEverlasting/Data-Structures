"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
        return self

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def delete(self, node):
        if not node.prev and not node.next:
            self.head = None
            self.tail = None
        elif not node.prev:
            self.head = node.next
        elif not node.next:
            self.tail = node.prev
        return node.delete()

    def add_to_head(self, value):
        self.length += 1
        if self.head:
            self.head.prev = ListNode(value, None, self.head)
            self.head = self.head.prev
        else:
            self.head = ListNode(value)
            self.tail = ListNode(value)

    def remove_from_head(self):
        if self.length == 0:
            return None
        else:
            self.length -= 1
            return self.delete(self.head)

    def add_to_tail(self, value):
        self.length += 1
        if self.tail:
            self.tail.next = ListNode(value, None, self.tail)
            self.tail = self.tail.next
        else:
            self.head = ListNode(value)
            self.tail = ListNode(value)

    def remove_from_tail(self):
        if self.length == 0:
            return None
        else:
            self.length -= 1
            return self.delete(self.tail)

    def move_to_front(self, node):
        self.delete(node)
        self.add_to_head(node.value)

    def move_to_end(self, node):
        self.delete(node)
        self.add_to_tail(node.value)

    def get_max(self):
        pass