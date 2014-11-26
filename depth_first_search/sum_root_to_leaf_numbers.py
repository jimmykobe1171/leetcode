"""
**Problem description:**

    Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

    An example is the root-to-leaf path 1->2->3 which represents the number 123.

    Find the total sum of all root-to-leaf numbers.

    For example::
          1
         / \
        2   3

    The root-to-leaf path 1->2 represents the number 12.

    The root-to-leaf path 1->3 represents the number 13.

    Return the sum = 12 + 13 = 25.
"""

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        def dfs(node, total_count):
            if not node:
                return 0

            total_count = total_count*10 + node.val
            tmp = 0
            tmp += dfs(node.left, total_count) + dfs(node.right, total_count)
            return total_count if tmp == 0 else tmp

        return dfs(root, 0)

def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    ans = Solution().sumNumbers(root)
    print ans
    
if __name__ == '__main__':
    main()

            