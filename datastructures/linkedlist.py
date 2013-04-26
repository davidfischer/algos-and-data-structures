class ListOutOfRangeError(Exception):
    pass


class ListItem(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList(object):
    def __init__(self):
        self.head = None

    # This could be implemented better as an instance counter
    # which is incremented on insert and decremented on remove
    def size(self):
        num = 0
        current = self.head
        while current is not None:
            num += 1
            current = current.next

        return num

    def index(self, value):
        num = 0
        current = self.head

        while current is not None:
            if current.value == value:
                return num
            current = current.next
            num += 1

        return None

    def insert(self, value, index):
        current = self.head
        previous = None
        for i in xrange(index):
            if current is not None:
                previous = current
                current = current.next
            else:
                raise ListOutOfRangeError()

        item = ListItem(value, current)
        if previous is not None:
            previous.next = item
        else:
            self.head = item
       
    def get(self, index):
        current = self.head
        for i in xrange(index):
            if current is not None:
                current = current.next
            else:
                raise ListOutOfRangeError()

        if current is not None:
            return current.value
        else:
            raise ListOutOfRangeError()

    def remove(self, index):
        current = self.head
        previous = None
        for i in xrange(index):
            if current is not None:
                previous = current
                current = current.next
            else:
                raise ListOutOfRangeError()
            
        if current is not None:
            if previous is not None:
                # removing index>0
                previous.next = current.next
            else:
                # removing index=0
                self.head = current.next
        else:
            # remove called on empty list
            raise ListOutOfRangeError()

        return current.value
