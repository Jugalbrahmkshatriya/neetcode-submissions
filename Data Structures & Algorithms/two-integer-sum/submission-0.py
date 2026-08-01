class Solution:
    def twoSum(self,nums: list[int],target:int) -> list[int]:
        a={} #number:{index}
        for i, j in enumerate(nums):
            diff=target-j
            if diff in a:
                return[a[diff],i]
            a[j]=i