"""
**Problem description:**

    Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

    If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

    You may not alter the values in the nodes, only nodes itself may be changed.

    Only constant memory is allowed.

    For example,
    Given this linked list: 1->2->3->4->5

    For k = 2, you should return: 2->1->4->3->5

    For k = 3, you should return: 3->2->1->4->5
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        new_head = ListNode(0)
        new_head.next = head
        slow_pointer = new_head
        fast_pointer = head
        if not head or not k:
            return head

        count = k
        while fast_pointer.next:
            if count == 1:
                # move to next k group
                count = k
                slow_pointer = fast_pointer
                fast_pointer = fast_pointer.next
            else:
                # reverse nodes
                current_node =fast_pointer.next
                tmp_node = slow_pointer.next
                slow_pointer.next = current_node
                fast_pointer.next = current_node.next
                current_node.next = tmp_node
                count -= 1
            
        if count > 1:
            # reverse last k group
            fast_pointer = slow_pointer.next
            while fast_pointer.next:
                # reverse nodes
                current_node =fast_pointer.next
                tmp_node = slow_pointer.next
                slow_pointer.next = current_node
                fast_pointer.next = current_node.next
                current_node.next = tmp_node

        return new_head.next

def loop_linked_list(head):
    while head is not None:
        print head.val
        head = head.next

def main():
    node_1 = ListNode(1)
    # node_2 = ListNode(2)
    # node_3 = ListNode(3)
    # node_4 = ListNode(4)
    # node_5 = ListNode(5)
    # node_1.next = node_2
    # node_2.next = node_3
    # node_3.next = node_4
    # node_4.next = node_5
    # loop_linked_list(node_1)
    
    ans = Solution().reverseKGroup(node_1, 3)
    # print ans
    loop_linked_list(ans)

if __name__ == '__main__':
    main()
                    