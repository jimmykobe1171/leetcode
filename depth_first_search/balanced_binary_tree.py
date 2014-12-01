"""
**Problem description:**

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

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
    def isBalanced(self, root):
        def is_balanced(node, cur_depth):
            if not node:
                return True, cur_depth

            cur_depth += 1
            left, left_depth = is_balanced(node.left, cur_depth)
            right, right_depth = is_balanced(node.right, cur_depth)
            if left and right and abs(left_depth - right_depth) <= 1:
                if left_depth >= right_depth:
                    return True, left_depth
                else:
                    return True, right_depth
            else:
                return False, None

        ans, depth = is_balanced(root, 0)
        return ans