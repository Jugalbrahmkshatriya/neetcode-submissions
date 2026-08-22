class Solution:
  def minEatingSpeed(self, piles: List[int], h: int) -> int:
    l, r = 1, max(piles)
    res = r
    while l <= r:
      k = (l + r) // 2
      hours = sum((p + k - 1) // k for p in piles)
      if hours <= h:
        res = k
        r = k - 1
      else:
        l = k + 1
    return res