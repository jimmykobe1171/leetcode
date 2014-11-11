# Swap Nodes in Pairs

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param a ListNode
    # @return a ListNode

    def swapPairs(self, head):
        current_node = ListNode(0)
        current_node.next = head
        first_node = current_node

        while current_node.next and current_node.next.next:
            # swap nodes
            node_1 = current_node.next
            node_2 = current_node.next.next
            node_1.next = node_2.next
            node_2.next = node_1
            current_node.next = node_2
            current_node = current_node.next.next

        return first_node.next
        

def loop_linked_list(head):
    while head is not None:
        print head.val
        head = head.next

def main():
    node_1 = ListNode(1)
    node_2 = ListNode(2)
    node_3 = ListNode(3)
    node_4 = ListNode(4)
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    # loop_linked_list(node_1)
    
    ans = Solution().swapPairs(node_1)
    loop_linked_list(ans)

if __name__ == '__main__':
    main()
