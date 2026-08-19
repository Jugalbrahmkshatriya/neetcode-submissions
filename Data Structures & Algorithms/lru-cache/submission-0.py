class LRUCache:
  def __init__(self, capacity: int):
    self.cap = capacity
    self.cache = {}
  def get(self, key: int) -> int:
    if key not in self.cache:
      return -1
    val = self.cache.pop(key)
    self.cache[key] = val
    return val
  def put(self, key: int, value: int) -> None:
    if key in self.cache:
      self.cache.pop(key)
    self.cache[key] = value
    if len(self.cache) > self.cap:
      first_key = next(iter(self.cache))
      self.cache.pop(first_key)