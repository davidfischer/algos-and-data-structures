class TrieNode(object):
    def __init__(self, edge):
        self.edge = edge
        self.children = []

    def __repr__(self):
        return u'<TrieNode: %s>' %(str(self))

    def __str__(self):
        return u'%s, children=[%s]' %(unicode(self.edge),
            unicode(', '.join([unicode(n.edge) for n in self.children])))


class Trie(object):
    """
    Implements a string based trie where edges correspond to the traversal
    values with any terminal nodes having an outgoing null (None) edge.
    """

    def __init__(self):
        self.root = TrieNode('')

    def insert(self, value):
        current = self.root
        for ch in value:
            child = None
            # check if the edge already exists
            for c in current.children:
                if c.edge == ch:
                    child = c
                    break

            # append this node even if it isn't a terminal node
            if child is None:
                c = TrieNode(ch)
                current.children.append(c)
                child = c

            current = child

        # make this node a terminal node
        if None not in [n.edge for n in current.children]:
            tn = TrieNode(None)
            current.children.append(tn)

    def remove(self, value):
        # FIXME: only removes the terminal 'None'
        current = self.root
        for ch in value:
            for child in current.children:
                if child.edge == ch:
                    current = child
                    break
            else:
                return None

        for i, node in enumerate(current.children):
            if node.edge is None:
                del current.children[i]

        return None

    def lookup(self, value):
        result = []
        current = self.root
        for ch in value:
            for child in current.children:
                if child.edge == ch:
                    current = child
                    result.append(child.edge)
                    break
            else:
                return None

        if None in [n.edge for n in current.children]:
            return ''.join(result)

        return None

    def __str__(self):
        result = []
        queue = []
        queue.append(self.root)
        while len(queue) > 0:
            current = queue.pop()
            result.append(unicode(current))
            for child in current.children:
                queue.append(child)
            
        return ''.join(result)
