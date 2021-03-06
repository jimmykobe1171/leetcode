"""
**Problem description:**

    Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

    For example, this binary tree is symmetric::

            1
           / \
          2   2
         / \ / \
        3  4 4  3

    But the following is not::

            1
           / \
          2   2
           \   \
           3    3

    Note:

    Bonus points if you could solve it both recursively and iteratively.

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
    def isSymmetric(self, root):
        def is_symmetric(left, right):
            if not left and not right:
                return True
            if  not left or not right:
                return False

            if left.val == right.val:
                out_pair = is_symmetric(left.left, right.right)
                in_pair = is_symmetric(left.right, right.left)
                return out_pair and in_pair
            else:
                return False

        if root:
            return is_symmetric(root.left, root.right)
        else:
            return True
