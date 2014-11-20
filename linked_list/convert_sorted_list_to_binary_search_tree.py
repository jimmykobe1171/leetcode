"""
**Problem description:**
    Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
"""

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        # return '%d, %s, %s' % (self.val, str(self.left), str(self.right))
        return str(self.val)
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        # get the linked list length
        next_node = head
        count = 0
        while next_node:
            count += 1
            next_node = next_node.next
        if count == 0 or count == 1:
            return head

        # print 'length:', count 

        # construct bst
        def construct_bst(node, start, end):
            print start, end
            if start > end:
                return None
            mid = (start + end) / 2
            left_child = construct_bst(node, start, mid-1)
            parent = TreeNode(node.val)
            parent.left = left_child
            # print 'node val:', parent.val
            # print 'before node:', node.val
            node = node.next
            # print 'after node:', node.val

            parent.right = construct_bst(node, mid+1, end)
            print '!!!!!!!!!!!!!'
            print start, end

            print 'parent: %d, left: %s, right:%s' %(parent.val, str(parent.left), str(parent.right))
            print 'node val:', node.val

            return parent

        return construct_bst(head, 0, count-1)


def inorder_traverse(node):
    if node:
        inorder_traverse(node.left)
        print node
        inorder_traverse(node.right)
    else:
        return

def main():
    node_1 = ListNode(1)
    node_2 = ListNode(2)
    node_3 = ListNode(3)
    node_4 = ListNode(4)
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4

    ans = Solution().sortedListToBST(node_1)
    # print ans
    # inorder_traverse(ans)

if __name__ == '__main__':
    main()

