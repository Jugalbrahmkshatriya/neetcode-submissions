class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        count1 = [0] * 26
        count2 = [0] * 26
        # Build initial frequency counts for s1 and the first window of s2
        for i in range(n1):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1
        # Slide the window across s2
        for i in range(n2 - n1):
            if count1 == count2:
                return True
            # Remove character leaving the window on the left
            count2[ord(s2[i]) - ord('a')] -= 1
            # Add character entering the window on the right
            count2[ord(s2[i + n1]) - ord('a')] += 1
        # Check the last window
        return count1 == count2