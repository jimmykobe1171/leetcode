# Reverse Linked List II

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        head_node = ListNode(0)
        head_node.next = head
        # next_node = head_node
        begin_node = None
        end_node = None
        # count = 0
        # while next_node.next:
        #     current_node = next_node.next
        #     count += 1
        #     if count == m:
        for i in range(m-1):
            head_node = head_node.next

        begin_node = head_node
        end_node = head_node.next
        for i in range(m-n):
            # swap nodes
            switch_node = end_node.next
            tmp_node = switch_node.next
            switch_node.next = begin_node.next
            begin_node.next = switch_node
            switch_node.next = end_node
            end_node.next = tmp_node


