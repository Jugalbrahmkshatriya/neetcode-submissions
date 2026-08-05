class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * len(nums)
        # Pass 1: Prefix products (left to right)
        p = 1
        for i in range(len(nums)):
            res[i] = p
            p *= nums[i]
        # Pass 2: Suffix products (right to left)
        s = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= s
            s *= nums[i]
        return res