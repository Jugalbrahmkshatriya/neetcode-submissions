class Solution:
  def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
    # Pair position with speed and sort descending by position
    pair = sorted(zip(position, speed), reverse=True)
    stack = []

    for p, s in pair:
      time = (target - p) / s
      stack.append(time)
      # If current car takes less/equal time than the fleet ahead,
      # it catches up and merges into that fleet.
      if len(stack) >= 2 and stack[-1] <= stack[-2]:
        stack.pop()

    return len(stack)