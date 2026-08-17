# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Dummy node handles edge cases like removing the head node
        dummy = ListNode(0, head)
        fast = head
        slow = dummy
        # Advance fast pointer n steps ahead
        for i in range(n):
            fast = fast.next
        # Move both pointers until fast reaches the end
        while fast:
            fast = fast.next
            slow = slow.next
        # Skip the nth node from the end
        slow.next = slow.next.next

        return dummy.next