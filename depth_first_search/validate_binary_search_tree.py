"""
**Problem description:**

    Given a binary tree, determine if it is a valid binary search tree (BST).

    Assume a BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than the node's key.

    The right subtree of a node contains only nodes with keys greater than the node's key.

    Both the left and right subtrees must also be binary search trees.
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        def is_in_range(node, min, max):
            if not node:
                return True
            if min < node.val and node.val < max:
                return is_in_range(node.left, min, node.val) and is_in_range(node.right, node.val, max)
            else:
                return False

        MIN = -1000000000000
        MAX = 1000000000000
        return is_in_range(root, MIN, MAX)

