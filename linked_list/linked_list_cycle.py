# Linked List Cycle

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        # stupid method of O(N) complexity and O(N) space
        # visited = {}
        # while head:
        #     if visited.get(head):
        #         return True

        #     visited[head] = True
        #     head = head.next
        #     print visited

        # return False

        # faster and slower pointer with O(N) complexity and O(1) space
        faster = head
        slower = head

        while slower and slower.next and faster and faster.next and faster.next.next:
            faster = faster.next.next
            slower = slower.next
            if faster == slower:
                return True

        return False

def main():
    node_1 = ListNode(1)
    node_2 = ListNode(2)
    node_1.next = node_2
    node_2.next = node_1
    # loop_linked_list(node_1)
    
    ans = Solution().hasCycle(node_1)
    print ans

if __name__ == '__main__':
    main()