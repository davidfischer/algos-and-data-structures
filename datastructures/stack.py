class EmptyStackError(Exception):
    pass

class StackItem(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class Stack(object):
    def __init__(self):
        self.head = None

    def push(self, value):
        self.head = StackItem(value, self.head)

    def pop(self):
        if self.empty():
            raise EmptyStackError

        result = self.head.value
        self.head = self.head.next
        return result

    def top(self):
        if self.empty():
            raise EmptyStackError

        return self.head.value

    def empty(self):
        return self.head is None
