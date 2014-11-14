# Remove Duplicates from Sorted List II

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        new_head = ListNode(0)
        new_head.next = head
        next_node = new_head
        while next_node.next:
            current_node = next_node.next
            compare_node = current_node
            while compare_node.next and current_node.val == compare_node.next.val:
                compare_node = compare_node.next
            if compare_node != current_node:
                # delete duplicate node
                next_node.next = compare_node.next
            else:
                next_node = next_node.next

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
    
    ans = Solution().deleteDuplicates(node_1)
    loop_linked_list(ans)

if __name__ == '__main__':
    main()

