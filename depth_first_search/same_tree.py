"""
**Problem description:**

    Given two binary trees, write a function to check if they are equal or not.

    Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if p and q:
            if p.val == q.val:
                left = self.isSameTree(p.left, q.left)
                right = self.isSameTree(p.right, q.right)
                return left and right
            else:
                return False
        elif not p and not q:
            return True
        else:
            return False
