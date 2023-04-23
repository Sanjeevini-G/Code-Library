class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def pre_order_traversal(node):
    if node is not None:
        print(node.value)
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)

# Example binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Traverse the binary tree in pre-order
pre_order_traversal(root)
