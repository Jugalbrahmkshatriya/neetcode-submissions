class TimeMap:
    def __init__(self):
        # Maps key -> list of [value, timestamp]
        self.store = {}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        # Since timestamps are strictly increasing, simply append
        self.store[key].append([value, timestamp])
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        # If the key doesn't exist, return empty string
        values = self.store.get(key, [])
        # Binary search for the closest timestamp <= target timestamp
        left, right = 0, len(values) - 1
        while left <= right:
            mid = (left + right) // 2
            # Check if current timestamp is <= target timestamp
            if values[mid][1] <= timestamp:
                res = values[mid][0]  # Store candidate value
                left = mid + 1        # Try finding a larger timestamp <= target
            else:
                right = mid - 1       # Timestamp too large, look left
        return res