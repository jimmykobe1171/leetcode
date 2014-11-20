"""
**Problem description:**
    You are given two linked lists representing two non-negative numbers. 

    The digits are stored in reverse order and each of their nodes contain a single digit.

    Add the two numbers and return it as a linked list.

    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)

    Output: 7 -> 0 -> 8
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        new_head = ListNode(0)
        head = new_head
        tmp_sum = 0
        while l1 or l2:
            tmp_sum /= 10
            if l1:
                tmp_sum += l1.val
                l1 = l1.next
            if l2:
                tmp_sum += l2.val
                l2 = l2.next

            head.next = ListNode(tmp_sum % 10)
            head = head.next

        if tmp_sum / 10 > 0:
            head.next = ListNode(1)

        return new_head.next

def loop_linked_list(head):
    while head is not None:
        print head.val
        head = head.next

def main():
    node_1 = ListNode(2)
    node_2 = ListNode(4)
    node_3 = ListNode(3)
    node_4 = ListNode(5)
    node_5 = ListNode(6)
    node_6 = ListNode(4)
    node_1.next = node_2
    node_2.next = node_3
    node_4.next = node_5
    node_5.next = node_6
    # loop_linked_list(node_1)
    
    ans = Solution().addTwoNumbers(node_1, node_4)
    # print ans
    loop_linked_list(ans)

if __name__ == '__main__':
    main()
