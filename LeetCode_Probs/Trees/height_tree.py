def height(node):
    if node is None:
        return -1  # An empty tree has height -1
    else:
        left_height = height(node.left)
        right_height = height(node.right)
        return max(left_height, right_height) + 1
