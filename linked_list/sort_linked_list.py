# Sort a linked list in O(n log n) time using constant space complexity.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        def merge(head, m, tail, n):


        def sort(head, n):
            if n < 2:
                return head.next

            next = sort(head, n/2)
            tail = sort(next, n/2)
            head, tail = merge(head, n/2, next, n/2)
            return head, tail

        # first_node = ListNode(0)
        # first_node.next = head
        n = 1
        next = head
        while next:
            current_head, tail = sort(next, n)
            if tail:
                sort(tail, n)
                head, tail = merge(head, n, tail, n)
            else:
                head = current_head

            next = tail
            n *= 2

        return head