class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
        from collections import Counter
        # Track needed character frequencies
        t_count = Counter(t)
        missing = len(t)
        start_idx = 0
        min_len = float("inf")
        l = 0
        for r, char in enumerate(s):
            # If the character is part of target `t`, update needed count
            if t_count[char] > 0:
                missing -= 1
            # Decrement frequency (unneeded characters go negative)
            t_count[char] -= 1
            # Try to shrink window as long as all required characters are present
            while missing == 0:
                if (r - l + 1) < min_len:
                    min_len = r - l + 1
                    start_idx = l
                # Pop left character from window
                t_count[s[l]] += 1
                if t_count[s[l]] > 0:
                    missing += 1
                l += 1
        return "" if min_len == float("inf") else s[start_idx : start_idx + min_len]