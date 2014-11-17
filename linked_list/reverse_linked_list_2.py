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
        new_head = head_node
        begin_node = None
        end_node = None
        for i in range(m-1):
            head_node = head_node.next

        begin_node = head_node
        end_node = head_node.next
        for i in range(n-m):
            # swap nodes
            switch_node = end_node.next
            tmp_node = switch_node.next
            switch_node.next = begin_node.next
            begin_node.next = switch_node
            end_node.next = tmp_node

        return new_head.next

def loop_linked_list(head):
    while head is not None:
        print head.val
        head = head.next

def main():
    node_1 = ListNode(5)
    node_2 = ListNode(4)
    node_3 = ListNode(3)
    node_4 = ListNode(-1)
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    # loop_linked_list(node_1)
    
    ans = Solution().reverseBetween(node_1, 1, 4)
    # print ans
    loop_linked_list(ans)

if __name__ == '__main__':
    main()