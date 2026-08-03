class Solution:
    def hasDuplicate(self, b: List[int]) -> bool:
        a = set()
        for num in b:
            if num in a:
                return True
            a.add(num)
        return False