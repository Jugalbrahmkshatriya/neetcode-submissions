class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n - 2):
            # Early exit: since the array is sorted, if the anchor element 
            # is positive, no three numbers can sum to 0.
            if nums[i] > 0:
                break   
            # Skip duplicates for the first element (i)
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # Skip duplicate values for the second element (left)
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                        
        return res