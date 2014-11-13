# Rotate List 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        head_node = head
        new_head = None
        length = 0

        while head_node:
            length += 1
            head_node = head_node.next

        if length == 0 or k == 0 or k % length == 0:
            return head

        k = k % length
        fast_node = head
        slow_node = head
        for i in range(k):
            fast_node = fast_node.next

        while fast_node.next:
            fast_node = fast_node.next
            slow_node = slow_node.next

        new_head = slow_node.next
        slow_node.next = None
        fast_node.next = head

        return new_head

def loop_linked_list(head):
    while head is not None:
        print head.val
        head = head.next

def main():
    node_1 = ListNode(5)
    # node_2 = ListNode(4)
    # node_3 = ListNode(3)
    # node_4 = ListNode(1)
    # node_1.next = node_2
    # node_2.next = node_3
    # node_3.next = node_4
    # loop_linked_list(node_1)
    
    ans = Solution().rotateRight(node_1, 2)
    loop_linked_list(ans)

if __name__ == '__main__':
    main()


