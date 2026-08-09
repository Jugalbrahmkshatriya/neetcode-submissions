class Solution:
  def isValid(self, s: str) -> bool:
    # Odd length strings can never form complete matching pairs
    if len(s) % 2 != 0:
      return False
    stack = []
    a = {")": "(", "]": "[", "}": "{"}
    for i in s:
      if i in a:
        if stack and stack[-1] == a[i]:
          stack.pop()
        else:
          return False
      else:
        stack.append(i)
    return not stack  # Returns True if stack is empty, False otherwise