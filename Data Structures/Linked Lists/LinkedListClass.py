

# Linked List advantages:
#    -Dynamic Size
#    -Ease of insertion/deletion
#
# Drawbacks:
#     -Random access not allowed. Must be sequential
#     -Pointer takes extra memory space
#     -Not cache friendly. Elements all over the place in memory
class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

    # Evaluation as string
    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None  # Prepending does not require copying whole new list, because links go one way
        # self.tail = None  # Tail is optional, only use if accessing from tail frequently, because appending
        # requires copying whole new list if nodes are immutable Tail is useless for stacks and queues. Also ruins
        # immutability and contiguity https://softwareengineering.stackexchange.com/questions/293525/is-there-any
        # -practical-way-for-a-linked-node-structure-to-be-immutable/293531#293531 Link for questions about
        # immutability and contiguity
        if nodes:
            self.head = Node(nodes.pop(0))
            node = self.head
            for elem in nodes:
                node.next_node = Node(elem)
                node = node.next_node

    # Prints linked list as node --> next node --> next node...
    def __repr__(self):
        node = self.head
        list = 'Empty'
        if node:
            list = ''
            while node is not None:
                list = list + f'{node} --> '
                node = node.next_node
            list = list + 'None'
        return list

    # Transversing linked list
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next_node

    def preappend(self, node):
        node.next_node = self.head
        self.head = node

    def append(self, node):
        if not self.head:
            self.head = node
            return
        for i in self:
            pass
        i.next_node = node

    def add_after(self, target_node_data, node):
        pass



test = LinkedList(['a','b','c','d','e'])
test.append(Node('asd'))
print(test)