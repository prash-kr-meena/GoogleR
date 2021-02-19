# https://www.geeksforgeeks.org/write-a-c-program-to-find-the-maximum-depth-or-height-of-a-tree/

# Binary 1GenericTree Node
class Node:
    def __init__(self, data):  # Constructor
        self.data = data
        self.left = None
        self.right = None


# My Hypothesis : That my height function will give the height of the 1GenericTree for that particular Node
def height(root) -> int:
    if root is None:
        return 0

    left_height = height(root.left)
    right_height = height(root.right)
    return 1 + max(left_height, right_height)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    root.left.right.left = Node(6)
    root.left.right.right = Node(7)

    print("Height : ", height(root))

"""      1
        / \
      2    3
     / \
    4   5
    |
   / \
  6   7
"""
