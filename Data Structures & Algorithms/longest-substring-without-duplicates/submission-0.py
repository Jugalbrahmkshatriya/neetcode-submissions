class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}  # Maps character to its most recent index
        left = 0
        max_len = 0
        for right in range(len(s)):
            char = s[right]
            # If the character is inside the current window, move the left pointer past it
            if char in char_map and char_map[char] >= left:
                left = char_map[char] + 1
            # Update the character's latest index
            char_map[char] = right
            # Update the maximum length found so far
            max_len = max(max_len, right - left + 1)
        return max_len