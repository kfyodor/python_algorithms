class UnorderedLinkedList(object):

    class _Node(object):
        def __init__(self, data):
            print('SINGLE')
            self.data = data
            self.next = None

        def add_next(self, node):
            self.next = node

        def is_last_node(self):
            return self.next == None

        def __str__(self):
            return str(self.data)

    class _Head(object):
        def __init__(self):
            print('SINGLE')
            self.node = None;
            self.length = 0;

    def __init__(self):
        self.head = self._Head()

    def add(self, item):
        new_node = self._Node(item)

        if not self.is_empty():
            new_node.add_next(self.head.node)
            
        self.head.node = new_node
        self.head.length += 1

    def get(self, index = 0):
        node = self.head.node

        for i in range(0, index):
            if node != None:
                node = node.next

        return node

    def is_empty(self):
        return len(self) == 0

    def append(self, item):
        node = self._Node(item)
        self.last().next = node
        self.head.length += 1

    def last(self):
        node = self.head.node

        while not node.is_last_node():
            node = node.next

        return node

    def search(self, data):
        node  = self.head.node

        if node.data == data: return True

        while not node.is_last_node():
            node = node.next
            if node.data == data: return True

        return False

    def pop(self, index = None):
        if index and index > self.head.length - 1: 
            raise 'Index is out of range'
        if self.head.length == 0:
            raise 'Can\'t pop from an empty list'

        index = index or self.head.length - 1
        
        if index == 0:
            node = self.head.node
            self.head.node = node.next
        else:
            temp_node = self.get(index - 1)
            node = temp_node.next
            temp_node.next = node.next

        self.head.length -= 1

        return node


    def remove(self, item):
        previous_node, current_node = (None, self.head.node)
        found = False

        while not found and not current_node == None:
            if current_node.data == item:
                found = True
            else:
                previous_node = current_node
                current_node = current_node.next

        if found:
            if current_node.is_last_node():
                previous_node.add_next(None)
            elif previous_node == None:
                self.head.node = current_node.next
            else:
                previous_node.add_next(current_node.next)

            self.head.length -= 1



    def __len__(self):
        return self.head.length

    def __str__(self):
        result, current_node = ([], self.head.node)

        result.append(current_node.data)

        while not current_node.is_last_node():
            current_node = current_node.next
            result.append(current_node.data)
            

        return "->".join(map(str, result))

class OrderedLinkedList(UnorderedLinkedList):
    def add(self, item): 
        previous_node, current_node = (None, self.head.node)
        stop = False

        while not stop and not current_node == None:
            if current_node.data > item:
                stop = True
            else:
                previous_node = current_node
                current_node = current_node.next

        node = self._Node(item)

        if previous_node:
            previous_node.next = node
        else:
            self.head.node = node

        node.next = current_node

        self.head.length += 1

        return True

    def append(self, item):
        raise NotImplemented

class DoubleLinkedList(object):
    class _Node(object):
        def __init__(self, data):
            self.next     = None
            self.previous = None
            self.data     = data

        def set_next(self, node):
            self.next = node
            if node: node.previous = self
                

        def set_previous(self, node):
            self.previous = node
            if node: node.next = self

        def is_first_node(self):
            return self.previous == None

        def is_last_node(self):
            return self.next == None

        def __str__(self):
            return str(self.data)

    def __init__(self):
        self.head   = None
        self.tail   = None
        self.length = 0

    def _set_head(self, node):
        self.head = node

        if node:
            self.head.set_previous(None)
        else:
            self.tail = None

    def _set_tail(self, node):
        self.tail = node

        if node: 
            self.tail.set_next(None)
        else:
            self.head = None

    def _delete_node(self, node):
        if not node: return

        if node.is_first_node():
            self._set_head(node.next)
        elif node.is_last_node():
            self._set_tail(node.previous)
        else:
            prev, next = node.previous, node.next
            prev.set_next(next)

        self.length -= 1

    def add(self, data):
        node = self._Node(data)

        if self.head == None:
            self.tail = self.head = node
        elif self.head.is_last_node():
            node.set_next(self.tail)
            self.head = node
        else:
            node.set_next(self.head)
            self.head = node

        self.length += 1


    def append(self, data):
        node = self._Node(data)

        if self.tail == None:
            self.tail = self.head = node
        elif self.tail.is_first_node():
            node.set_previous(self.head)
            self.tail = node
        else:
            node.set_previous(self.tail)
            self.tail = node

        self.length += 1

    def remove(self, data):
        current_node = self.head
        found        = False

        while current_node != None and not found:
            if current_node.data == data:
                found = True
            else:
                current_node = current_node.next

        if found:
            self._delete_node(current_node)

        return found

    def pop(self, index = None):
        node = self.get(index) if index else self.tail

        self._delete_node(node)
        return node

    def get(self, index = 0):
        node = self.head

        for i in range(0, index):
            if node != None:
                node = node.next

        return node

    def is_empty(self):
        return self.head == None

    def __len__(self):
        return self.length

    def __str__(self):
        result, current_node = ([], self.head)

        if not self.is_empty():
            result.append(current_node.data)

            while not current_node.is_last_node():
                current_node = current_node.next
                result.append(current_node.data)


        return "[" + " <-> ".join(map(str, result)) + "]"
