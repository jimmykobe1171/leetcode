# Remove Duplicates from Sorted List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        head_node = ListNode(0)
        head_node.next = head
        new_head = head_node
        while head_node.next:
            current_node = head_node.next
            next_node = current_node.next
            while next_node and current_node.val == next_node.val:
                next_node = next_node.next
            current_node.next = next_node
            head_node = head_node.next

        return new_head.next

def loop_linked_list(head):
    while head is not None:
        print head.val
        head = head.next

def main():
    node_1 = ListNode(1)
    # node_2 = ListNode(1)
    # node_3 = ListNode(3)
    # node_4 = ListNode(3)
    # node_1.next = node_2
    # node_2.next = node_3
    # node_3.next = node_4
    # loop_linked_list(node_1)
    
    ans = Solution().deleteDuplicates(node_1)
    loop_linked_list(ans)

if __name__ == '__main__':
    main()

