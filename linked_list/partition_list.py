# Partition List 
"""
**Problem description:**
    Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

    You should preserve the original relative order of the nodes in each of the two partitions.

    For example,
    Given 1->4->3->2->5->2 and x = 3,
    return 1->2->2->4->3->5.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        new_head = ListNode(0)
        new_head.next = head
        pointer_slow = new_head
        pointer_fast = new_head
        while pointer_fast.next:
            if pointer_fast.next.val < x:
                if pointer_slow == pointer_fast:
                    pointer_fast = pointer_fast.next
                    pointer_slow = pointer_slow.next
                    continue

                # insert after pointer slow
                tmp_node = pointer_slow.next
                pointer_slow.next = pointer_fast.next
                pointer_fast.next = pointer_fast.next.next
                pointer_slow.next.next = tmp_node
                # update pointer position
                pointer_slow = pointer_slow.next
            else:
                pointer_fast = pointer_fast.next

        return new_head.next

def loop_linked_list(head):
    while head is not None:
        print head.val
        head = head.next

def main():
    node_1 = ListNode(5)
    node_2 = ListNode(4)
    node_3 = ListNode(3)
    node_4 = ListNode(1)
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    # loop_linked_list(node_1)
    
    ans = Solution().partition(node_1, 6)
    # print ans
    loop_linked_list(ans)

if __name__ == '__main__':
    main()