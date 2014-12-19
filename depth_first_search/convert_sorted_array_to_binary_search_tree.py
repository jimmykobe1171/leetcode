"""
**Problem description:**

    Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
"""

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        def array_to_bst(array, begin, end):
            if begin > end:
                return None

            mid = (begin + end) / 2
            mid_node = TreeNode(array[mid])
            left_node = array_to_bst(array, begin, mid-1)
            right_node = array_to_bst(array, mid+1, end)
            mid_node.left = left_node
            mid_node.right = right_node

            return mid_node

        return array_to_bst(num, 0, len(num)-1)
