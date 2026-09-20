# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Step 1: Pre-order serialization with unique delimiters
        def serialize(node: Optional[TreeNode]) -> str:
            if not node:
                return ",#"
            # Using commas and symbols ensures values like '1' and '12' aren't falsely matched
            return f",{node.val}" + serialize(node.left) + serialize(node.right)
        s_root = serialize(root)
        s_sub = serialize(subRoot)
        # Step 2: KMP string search algorithm
        return self.kmpSearch(s_root, s_sub)
    def kmpSearch(self, text: str, pattern: str) -> bool:
        if not pattern:
            return True
        # Build Longest Prefix Suffix (LPS) table
        lps = [0] * len(pattern)
        prev_lps, i = 0, 1
        while i < len(pattern):
            if pattern[i] == pattern[prev_lps]:
                lps[i] = prev_lps + 1
                prev_lps += 1
                i += 1
            elif prev_lps == 0:
                lps[i] = 0
                i += 1
            else:
                prev_lps = lps[prev_lps - 1]
        # Search pattern in text
        i = j = 0
        while i < len(text):
            if text[i] == pattern[j]:
                i += 1
                j += 1
            if j == len(pattern):
                return True
            elif i < len(text) and text[i] != pattern[j]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return False