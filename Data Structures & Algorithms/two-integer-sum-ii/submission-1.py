#solution for two integer sum-2 sorted array one 167 leetcode problem and 11/150 of neetcode 150
class Solution:

  def twoSum(self, numbers: list[int], target: int) -> list[int]:
    a= 0
    b=len(numbers) - 1

    while a < b:
      sum = numbers[a] + numbers[b]

      if sum == target:
        return [a+1, b+1]
      elif sum < target:
        a += 1  # Need a larger sum, move left pointer right
      else:
        b -= 1  # Need a smaller sum, move right pointer left