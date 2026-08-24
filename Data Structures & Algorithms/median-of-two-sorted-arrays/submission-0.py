class Solution:
  def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
    # Ensure nums1 is the smaller array to minimize the binary search range
    if len(nums1) > len(nums2):
      nums1, nums2 = nums2, nums1
    m, n = len(nums1), len(nums2)
    total = m + n
    half = (total + 1) // 2  # Works for both even and odd total lengths
    left, right = 0, m
    while left <= right:
      i = (left + right) // 2  # Elements taken from nums1
      j = half - i  # Elements taken from nums2
      # Boundary values (use -inf / +inf for out-of-bounds index positions)
      nums1_left = nums1[i - 1] if i > 0 else float('-inf')
      nums1_right = nums1[i] if i < m else float('inf')
      nums2_left = nums2[j - 1] if j > 0 else float('-inf')
      nums2_right = nums2[j] if j < n else float('inf')
      # Check if partition is valid
      if nums1_left <= nums2_right and nums2_left <= nums1_right:
        # Odd number of total elements
        if total % 2 != 0:
          return float(max(nums1_left, nums2_left))
        # Even number of total elements
        return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2.0
      # Too many elements taken from nums1, shift binary search left
      elif nums1_left > nums2_right:
        right = i - 1
      # Too few elements taken from nums1, shift binary search right
      else:
        left = i + 1