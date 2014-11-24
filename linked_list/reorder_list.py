# -*- coding: utf-8 -*-
"""
**Problem description:**

Given a singly linked list L: L0→L1→…→Ln-1→Ln,

reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,

Given {1,2,3,4}, reorder it to {1,4,2,3}.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing
    # 
    # now the algorithm is O(n) complexity and O(n) space
    # space could be improved to O(1) if we use slow and
    # fast pointer to locate list middle, and revert second
    # half of list, then insert reversed second half to 
    # first half
    def reorderList(self, head):
        new_head = ListNode(0)
        new_head.next = head
        result = new_head
        reverse_nodes = []
        # save reverse nodes in array
        while new_head.next:
            reverse_nodes.insert(0, new_head.next)
            new_head = new_head.next
        new_head = result.next

        length = len(reverse_nodes)
        if length == 0 or length == 1:
            return head

        count = length/2
        for i in range(0, count):
            # reorder list
            if i == count-1 and length%2 == 0:
                break
            insert_node = reverse_nodes[i]
            tmp_ndoe = new_head.next
            new_head.next = insert_node
            reverse_nodes[i+1].next = insert_node.next
            insert_node.next = tmp_ndoe
            new_head = tmp_ndoe

        return result.next

def loop_linked_list(head):
    while head is not None:
        print head.val
        head = head.next

def main():
    node_1 = ListNode(1)
    node_2 = ListNode(2)
    node_3 = ListNode(3)
    node_4 = ListNode(4)
    node_5 = ListNode(5)
    node_6 = ListNode(6)
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    node_5.next = node_6
    # loop_linked_list(node_1)
    
    ans = Solution().reorderList(node_1)
    # print ans
    loop_linked_list(ans)

if __name__ == '__main__':
    main()
