# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        # Step 1: Find the middle node using slow & fast pointers
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # Step 2: Split the list and reverse the second half
        second = slow.next
        slow.next = None  # Disconnect the two halves
        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        # Step 3: Merge the two halves (first: head, second: prev)
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2