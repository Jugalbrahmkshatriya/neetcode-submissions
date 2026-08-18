"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        # Pass 1: Interleave cloned nodes after original nodes (A -> A' -> B -> B')
        curr = head
        while curr:
            cloned = Node(curr.val, curr.next)
            curr.next = cloned
            curr = cloned.next
        # Pass 2: Connect random pointers for cloned nodes
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        # Pass 3: Separate original list and cloned list
        curr = head
        cloned_head = head.next
        while curr:
            cloned = curr.next
            curr.next = cloned.next
            if cloned.next:
                cloned.next = cloned.next.next
            curr = curr.next
        return cloned_head