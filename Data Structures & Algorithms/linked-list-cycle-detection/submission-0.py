class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = head  # s = slow (moves 1 step)
        f = head  # f = fast (moves 2 steps)
        while f and f.next:
            s = s.next
            f = f.next.next
            if s == f:
                return True
        return False