class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        if len(self.storage) == 0:
            return None
        deleted = self.storage.pop(0)
        if len(self.storage) > 0:
            from_end = self.storage.pop()
            self.storage.insert(0, from_end)
            self._sift_down(0)
        return deleted

    def get_max(self):
        if len(self.storage) == 0:
            return None
        else:
            return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        if index == 0:
            return
        child = self.storage[index]
        parent = self.storage[(index - 1) // 2]
        if parent < child:
            self.storage[index] = parent
            self.storage[(index - 1) // 2] = child
            self._bubble_up((index - 1) // 2)

    def _sift_down(self, index):
        if len(self.storage) < index * 2 + 2:
            return
        elif len(self.storage) == index * 2 + 2:
            parent = self.storage[index]
            left = self.storage[index * 2 + 1]
            right = None
        else:
            parent = self.storage[index]
            left = self.storage[index * 2 + 1]
            right = self.storage[index * 2 + 2]

        if right and right > left:
            if right > parent:
                self.storage[index * 2 + 2] = parent
                self.storage[index] = right
                self._sift_down(index * 2 + 2)
        elif left > parent:
            self.storage[index * 2 + 1] = parent
            self.storage[index] = left
            self._sift_down(index * 2 + 1)

