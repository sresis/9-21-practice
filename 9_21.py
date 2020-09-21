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

class LinkedList:
    def __init__(self):
        self.head = 'hi'
        self.tail = None
    


    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
        
        return None


 #test LL  
list_1 = LinkedList()
list_1.head = Node('apple')
b = Node('berry')
c = Node('cherry')
list_1.head.next = b
b.next = c

list_1.print_list()

