# Binary Tree- Data structure where each node has at most two children(left and right)
#       Complete Binary Tree- Every level(except possible last) is filled, and filled left to right
#       Full Binary Tree- Every single node has 0 or 2 children
# Can be transversed depth-first or breadth-first
# Three common ways to transverse depth first
#       Pre-order
#       In-order
#       Post-order


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == 'pre_order':
            print(self.pre_order(tree.root, ''))
        else:
            print('Traversal type doesnt exist')

    def pre_order(self, start, traversal):
        """
        Root -> Left -> Right
        1. Check if current node is empty
        2. Display data
        3. Transverse left subtree recursively
        4. Transverse right subtree recursively
        TLDR: Down left as far as you go, then right as far as you can go, then back up
        """
        if start:
            traversal += (str(start.value) + '-')
            traversal = self.pre_order(start.left, traversal)
            traversal = self.pre_order(start.right, traversal)
        return traversal


# 1-3-4-7-5-
#       1
#     /   \
#    3     5
#   /  \
#  4    7


tree = BinaryTree(1)
tree.root.left = Node(3)
tree.root.right = Node(5)
tree.root.left.left = Node(4)
tree.root.left.right = Node(7)
tree.print_tree('pre_order')