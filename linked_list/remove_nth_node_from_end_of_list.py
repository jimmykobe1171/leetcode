# Remove Nth Node From End of List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        if n == 0:
            return head
        head_node = ListNode(0)
        head_node.next = head
        new_head = head_node
        count = 0
        remove_node = None
        while head_node.next:
            if remove_node:
                remove_node = remove_node.next
            count += 1
            if count == n:
                remove_node = new_head
            head_node = head_node.next

        # remove node
        remove_node.next = remove_node.next.next
        return new_head.next

def loop_linked_list(head):
    while head is not None:
        print head.val
        head = head.next

def main():
    node_1 = ListNode(5)
    # node_2 = ListNode(4)
    # node_3 = ListNode(3)
    # node_4 = ListNode(-1)
    # node_1.next = node_2
    # node_2.next = node_3
    # node_3.next = node_4
    # loop_linked_list(node_1)
    
    ans = Solution().removeNthFromEnd(node_1, 1)
    print ans
    loop_linked_list(ans)

if __name__ == '__main__':
    main()