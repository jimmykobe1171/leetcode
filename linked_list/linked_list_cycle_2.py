# Linked List Cycle II
# tortoise and hare algorithm

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        faster_node = head
        slower_node = head
        while slower_node and faster_node and faster_node.next:
            slower_node = slower_node.next
            faster_node = faster_node.next.next
            if faster_node == slower_node:
                while head != slower_node:
                    head = head.next
                    slower_node = slower_node.next

                return head

        return None

