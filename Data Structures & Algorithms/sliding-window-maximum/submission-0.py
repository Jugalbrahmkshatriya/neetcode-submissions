class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if k == 1:
            return nums
        # Block boundary max arrays
        left = [0] * n
        right = [0] * n
        for i in range(n):
            # Fill left-to-right maxes for each block of size k
            if i % k == 0:
                left[i] = nums[i]
            else:
                left[i] = max(left[i - 1], nums[i])
            # Fill right-to-left maxes for each block of size k
            j = n - 1 - i
            if (j + 1) % k == 0 or j == n - 1:
                right[j] = nums[j]
            else:
                right[j] = max(right[j + 1], nums[j])
        # Construct the maximums for each sliding window
        return [max(right[i], left[i + k - 1]) for i in range(n - k + 1)]
