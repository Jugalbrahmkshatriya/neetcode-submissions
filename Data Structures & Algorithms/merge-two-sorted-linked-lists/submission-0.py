class Solution:
    def mergeTwoLists(self, a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
        d = ListNode()  # d = dummy starting node
        c = d           # c = current pointer (moving tail)
        while a and b:
            if a.val < b.val:
                c.next = a
                a = a.next
            else:
                c.next = b
                b = b.next
            c = c.next
        c.next = a or b  # attach whatever list still has letters left
        return d.next