"""
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root):
        MIN = -1
        def dfs(node, cur_sum, best):
            cur_sum += 1
            if not node.left and not node.right:
                if cur_sum > best:
                    best = cur_sum
                return best
            if node.left:
                best = dfs(node.left, cur_sum, best)
            if node.right:
                best = dfs(node.right, cur_sum, best)
            return best

        if not root:
            return 0
        else:
            return dfs(root, 0, MIN)