class Solution:

    def encode(self, strs: list[str]) -> str:
        # Concatenate each string prefixed by its length and a delimiter
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> list[str]:
        res, i = [], 0
        while i < len(s):
            # Find the position of the delimiter '#'
            j = s.find("#", i)
            length = int(s[i:j])
            # Extract the exact substring using the length
            res.append(s[j + 1 : j + 1 + length])
            # Move pointer past the current string
            i = j + 1 + length
        return res