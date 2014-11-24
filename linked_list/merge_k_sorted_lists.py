"""
**Problem description:**
    Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        def merge_two_list(l1, l2):
            new_head = ListNode(0)
            result = new_head
            while l1 and l2:
                if l1.val <= l2.val:
                    selected_node = l1
                    l1 = l1.next
                else:
                    selected_node = l2
                    l2 = l2.next

                new_head.next = selected_node
                new_head = new_head.next

            if l1:
                new_head.next = l1
            if l2:
                new_head.next = l2

            return result.next

        def merge_lists(lists, start, end):
            if start > end:
                return None
            if start == end:
                return lists[start]

            mid = (start + end) / 2
            l1 = merge_lists(lists, start, mid)
            l2 = merge_lists(lists, mid+1, end)
            if l1 and l2:
                return merge_two_list(l1, l2)
            else:
                return l1 or l2

        return merge_lists(lists, 0, len(lists)-1)


def loop_linked_list(head):
    while head is not None:
        print head.val
        head = head.next

def main():
    node_1 = ListNode(1)
    node_2 = ListNode(3)
    node_3 = ListNode(5)
    node_1.next = node_2
    node_2.next = node_3

    node_4 = ListNode(2)
    node_5 = ListNode(4)
    node_6 = ListNode(6)
    node_4.next = node_5
    node_5.next = node_6

    node_6 = ListNode(7)
    node_7 = ListNode(8)
    node_8 = ListNode(9)
    node_6.next = node_7
    node_7.next = node_8

    # lists = [node_1, node_4]
    lists = [node_1, node_4, node_6]
    
    ans = Solution().mergeKLists(lists)
    # print ans
    loop_linked_list(ans)

if __name__ == '__main__':
    main()

