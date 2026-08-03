class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Step 1: Quick length check
        if len(s) != len(t):
            return False
        # Step 2: Fixed array of size 26 for lowercase English letters
        counts = [0] * 26
        # Step 3: Populate counts balance
        for i in range(len(s)):
            counts[ord(s[i]) - ord('a')] += 1
            counts[ord(t[i]) - ord('a')] -= 1
        # Step 4: Validate all balances return to 0
        for count in counts:
            if count != 0:
                return False
        return True