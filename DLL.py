class Node(object):
    """Node in a linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "<Node object. Data: {}; Next: {}>".format(
                                        self.data,
                                        self.next.data if self.next else None,
                                        )

class DblLinkedList:
    """double linked list."""
    def __init__(self):
        self.head = None
        self.tail = None

    def remove(self, node_to_remove):
        """remove the node that has the value of the argument.""" 
        if node_to_remove == self.head:
            self.head = node_to_remove.next
        elif node_to_remove == self.tail:
            self.tail = node_to_remove.prev
        else:
            node_to_remove.prev = node_to_remove.next
        return None

#test LL  
list_1 = DblLinkedList()
list_1.head = Node('apple')
b = Node('berry')
c = Node('cherry')
list_1.head.next = b
b.next = c

list_1.remove(Node('apple'))
print(list_1.head)
print(list_1.head.next)