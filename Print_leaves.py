class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def print_leaves(node):
    if node is not None:
        if node.left is None and node.right is None:
            print(node.value)
        else:
            print_leaves(node.left)
            print_leaves(node.right)

# Example binary search tree
root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)
root.right.right = Node(14)
root.left.right.left = Node(4)
root.left.right.right = Node(7)
root.right.right.left = Node(13)

# Print all the leaves of the binary search tree
print_leaves(root)
