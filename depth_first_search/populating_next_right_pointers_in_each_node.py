"""
**Problem description:**

    Given a binary tree::

        struct TreeLinkNode {
          TreeLinkNode *left;
          TreeLinkNode *right;
          TreeLinkNode *next;
        }

    Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

    Initially, all next pointers are set to NULL.

    Note:

    You may only use constant extra space.

    You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).

    For example,

    Given the following perfect binary tree::

             1
           /  \
          2    3
         / \  / \
        4  5  6  7

    After calling your function, the tree should look like::

             1 -> NULL
           /  \
          2 -> 3 -> NULL
         / \  / \
        4->5->6->7 -> NULL

"""

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if not root:
            return root

        left_node = root
        while left_node.left:
            current_node = left_node
            current_node.left.next = current_node.right
            next_node = current_node.next
            while next_node:
                current_node.right.next = next_node.left
                next_node.left.next = next_node.right
                current_node = next_node
                next_node = next_node.next

            left_node = left_node.left


