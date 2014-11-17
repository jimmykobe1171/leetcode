# Merge Two Sorted Lists 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        new_list = None
        tail = None
        while l1 or l2:
            if l1 is None:
                selected_node = l2
                l2 = l2.next
            elif l2 is None:
                selected_node = l1
                l1 = l1.next
            elif l1.val <= l2.val:
                selected_node = l1
                l1 = l1.next
            else:
                selected_node = l2
                l2 = l2.next

            if not new_list:
                new_list = selected_node
                tail = new_list
            else:
                tail.next = selected_node
                tail = selected_node

        return new_list

