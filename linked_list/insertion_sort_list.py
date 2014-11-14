# Insertion Sort List 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if not head:
            return head

        new_head = ListNode(0)
        new_head.next = head
        next_node = head
        while next_node.next:
            if next_node.val <= next_node.next.val:
                next_node = next_node.next
            else:
                tmp_head = new_head
                while tmp_head.next.val <= next_node.next.val:
                    tmp_head = tmp_head.next
                # swap node, note that should not move next_node
                # to next
                tmp = tmp_head.next
                tmp_head.next = next_node.next
                next_node.next = next_node.next.next
                tmp_head.next.next = tmp

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
    
    ans = Solution().insertionSortList(node_1)
    # print ans
    loop_linked_list(ans)

if __name__ == '__main__':
    main()


