"""
**Problem description:**

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
"""

# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        current_node = RandomListNode(0)
        current_node.next = head
        new_list_head = RandomListNode(0)
        result = new_list_head
        mapping = {}

        while current_node.next:
            next_node = current_node.next
            # copy next node
            if next_node in mapping:
                tmp_node = mapping[next_node]
            else:
                tmp_node = RandomListNode(next_node.label)
                mapping[next_node] = tmp_node
            new_list_head.next = tmp_node
            # copy random node
            if current_node.random:
                if current_node.random in mapping:
                    random_node = mapping[current_node.random]
                else:
                    random_node = RandomListNode(current_node.random.label)
                    mapping[current_node.random] = random_node

                new_list_head.random = random_node

            # move to next node
            current_node = current_node.next
            new_list_head = new_list_head.next

        if current_node.random:
            new_list_head.random = mapping[current_node.random]

        return result.next

def loop_linked_list(head):
    while head is not None:
        print 'label:', head.label, 'ramdom:', head.random
        head = head.next

def main():
    node_1 = RandomListNode(-1)
    node_2 = RandomListNode(-1)
    # node_3 = RandomListNode(3)
    # node_4 = RandomListNode(5)
    # node_5 = RandomListNode(6)
    # node_6 = RandomListNode(4)
    node_1.next = node_2
    node_2.random = node_1
    # node_2.next = node_3
    # node_4.next = node_5
    # node_5.next = node_6
    # loop_linked_list(node_1)
    
    ans = Solution().copyRandomList(node_1)
    # print ans
    loop_linked_list(ans)

if __name__ == '__main__':
    main()
