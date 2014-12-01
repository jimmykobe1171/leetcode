"""
**Problem description:**

    Given a binary tree, find its minimum depth.

    The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        MAX = 10000000
        def dfs(node, cur_sum, best):
            cur_sum += 1
            if not node.left and not node.right:
                if cur_sum < best:
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
            return dfs(root, 0, MAX)
