class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Map frequency tuple to list of anagrams
        groups = {}
        for s in strs:
            # Count 26 character frequencies
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            # Use count tuple as dict key
            key = tuple(count)
            if key not in groups:
                groups[key] = []
            groups[key].append(s)
        return list(groups.values())