class MinStack:

  def __init__(self):
    self.stack: list[int] = []
    self.minStack: list[int] = []

  def push(self, val: int) -> None:
    self.stack.append(val)
    # Push to min_stack ONLY if val is <= current minimum.
    # Handles duplicate minimums correctly while saving memory.
    if not self.minStack or val <= self.minStack[-1]:
      self.minStack.append(val)

  def pop(self) -> None:
    # Synchronize min_stack only when the popped element is the current minimum.
    if self.stack.pop() == self.minStack[-1]:
      self.minStack.pop()

  def top(self) -> int:
    return self.stack[-1]

  def getMin(self) -> int:
    return self.minStack[-1]