class Deque:
    def __init__(self):
        self.items = []
    def add_front(self,i):
        self.items.append(i)
    def add_rear(self,i):
        self.items.insert(0,i)
    def remove_front(self):
        return self.items.pop()
    def remove_rear(self):
        return self.items.pop(0)
    def is_empty(self):
        return self.items == []
    def size(self):
        return len(self.items)




