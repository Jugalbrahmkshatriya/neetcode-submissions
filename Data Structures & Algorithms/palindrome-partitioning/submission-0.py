from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        
        # dp[i][j] = True if substring s[i:j+1] is a palindrome
        dp = [[False] * n for _ in range(n)]
        for r in range(n):
            for l in range(r + 1):
                if s[l] == s[r] and (r - l <= 2 or dp[l + 1][r - 1]):
                    dp[l][r] = True

        res, cur = [], []

        def dfs(i: int) -> None:
            if i == n:
                res.append(cur.copy())  # Valid partition found
                return

            for j in range(i, n):
                if dp[i][j]:            # Fast O(1) palindrome check
                    cur.append(s[i : j + 1])
                    dfs(j + 1)          # Recurse for remaining string
                    cur.pop()           # Backtrack

        dfs(0)
        return res