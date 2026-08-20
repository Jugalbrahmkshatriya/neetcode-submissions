class Solution:

    def findDuplicate(self, nums: list[int]) -> int:
        # Both pointers MUST start at index 0
        slow = 0
        fast = 0

        # Phase 1: Locate the intersection point in the cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Phase 2: Locate the entrance to the cycle (the duplicate number)
        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow