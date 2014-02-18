import functools

class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self, number = 1):
        if number < 1:
            raise 'Can\'t pop less than one item'
        elif number == 1: 
            return self.items.pop()

        return functools.reduce(
            lambda memo, _: 
                memo + [self.pop()]
            , range(0, number)
            , []
        )


    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.size() == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.items[len(self.items) - 1]

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return "[" + ", ".join(map(str, self.items)) + "]"