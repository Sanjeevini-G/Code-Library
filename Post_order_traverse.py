class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def post_order_traversal(node):
    if node is not None:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node.value)

# Example binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Traverse the binary tree in post-order
post_order_traversal(root)
