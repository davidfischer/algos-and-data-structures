class HashItem(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable(object):
    def __init__(self, initsize=100):
        self.initsize = initsize
        self.buckets = [None for i in xrange(initsize)]

    def insert(self, key, value):
        index = self._hash(key)
        item = HashItem(key, value)
        if self.buckets[index] is None:
            self.buckets[index] = [item]
            return value
        else:
            for elem in self.buckets[index]:
                if elem.key == key:
                    elem.value = value
                    return value
            self.buckets[index].append(item)

        return value

    def remove(self, key):
        index = self._hash(key)
        if self.buckets[index] is None:
            return None
        for elem in self.buckets[index]:
            if elem.key == key:
                self.buckets[index].remove(elem)
                return elem.value

        return None

    def lookup(self, key):
        index = self._hash(key)
        if self.buckets[index] is None:
            return None
        else:
            for elem in self.buckets[index]:
                if elem.key == key:
                    return elem.value

        return None

    # this may be better implemented as an an instance variable
    # which is incremented on insert and decremented on remove
    def size(self):
        elems = 0
        for bucket in self.buckets:
            if bucket is not None:
                elems += len(bucket)

        return elems

    def _hash(self, key):
        return abs(hash(key)) % (self.initsize - 1)
