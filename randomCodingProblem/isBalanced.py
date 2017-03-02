A tree is "superbalanced" if the difference between the depths of any two leaf nodes is no greater than one. Given the root of this tree figureout if this tree is "superbalanced"
"""

DIFFERENCE BETWEEN DEPTH OF ANY TWO LEAF NODES IS NO GREATER THAN ONE =
DIFFERENCE BETWEEN HEIGHT OF LEFT AND RIGHT SUBTREES ARE ALSO NO GREATER THAN ONE

1. Ensure that you're working with a binary tree
2. Ask about edge cases
3a. Pseudo code
3b. Actual code

class Node:
  def __init__(self, data, right=None, left=None):
      self.data = data
      self.right = right
      self.left = left

"""
    10
   7  12
  5 8   14
 3

    10
   7  12
  5 8   14
 9     3
  13
    43


def isBalanced(head):
    if head == None:
        return False

    leftHeight = height(head.left)
    rightHeight = height(head.right)

    // compare left and right subtrees
    if(abs(leftHeight - rightHeight) <= 1) and isBalanced(head.left) and isBalanced(head.right))
        return True

    return false


def isBalanced(head):
    if head == None:
        return False

    leftHeight = height(head.left)
    rightHeight = height(head.right)

    if(abs(leftHeight - rightHeight) <= 1) and isBalanced(head.left) and isBalanced(head.right))
        return True

    return false

def height(node):
    rightHeight = 0
    leftHeight = 0

    if node.left != None:
        leftHeight = 1 + height(node.left) # 4

    if node.right != None:
        rightHeight = 1 + height(node.right) # 3

    return max(leftHeight, rightHeight)

    http://www.geeksforgeeks.org/how-to-determine-if-a-binary-tree-is-balanced/
