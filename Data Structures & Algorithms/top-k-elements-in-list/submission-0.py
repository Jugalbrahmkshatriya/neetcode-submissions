class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count frequency of each number
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        # Group numbers by frequency (buckets)
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)
        # Collect top k frequent elements from highest frequency
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res