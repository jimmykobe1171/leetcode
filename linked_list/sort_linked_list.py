# Sort a linked list in O(n log n) time using constant space complexity.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):

        def merge(head_1, m, head_2, n):
            # print head_1, m, head_2, n

            head, tail = None, None
            while m + n > 0:
                if n == 0:
                    select_head = head_1
                    head_1 = head_1.next
                    m -= 1
                elif m == 0:
                    select_head = head_2
                    head_2 = head_2.next
                    n -= 1
                    # reset n if there are less than n nodes
                    if not head_2:
                        n = 0
                else:
                    if head_1.val <= head_2.val:
                        select_head = head_1
                        head_1 = head_1.next
                        m -= 1
                    else:
                        select_head = head_2
                        head_2 = head_2.next
                        n -= 1
                        # reset n if there are less than n nodes
                        if not head_2:
                            n = 0

                if not head:
                    head = select_head
                    tail = head
                else:
                    tail.next = select_head
                    tail = tail.next

            # revise the tail pointer
            tail.next = head_2
            tail = tail.next

            # print 'hhhhhhh', head, tail
            return head, tail

        # n must be even
        def sort(head, n):
            if n < 2:
                return head, head.next

            head_1, tail_1 = sort(head, n/2)
            if tail_1:
                head_2, tail_2 = sort(tail_1, n/2)
                head, tail = merge(head_1, n/2, head_2, n/2)
            else:
                head, tail = head_1, tail_1

            return head, tail

        if not head:
            return head

        step = 1
        next_node = head.next
        while next_node:
            head_1, tail_1 = sort(next_node, step)
            head, tail = merge(head, step, head_1, step)
            next_node = tail
            step *= 2
            # print next_node

        return head

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
    
    ans = Solution().sortList(node_1)
    loop_linked_list(ans)

if __name__ == '__main__':
    main()
