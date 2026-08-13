class Solution:
    def maxArea(self, heights: list[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_water = 0
        while left < right:
            # Width between the two pointers
            width = right - left
            # The height of the container is limited by the shorter line
            current_height = min(heights[left], heights[right])
            # Calculate stored water and update max_water
            current_water = width * current_height
            if current_water > max_water:
                max_water = current_water
            # Move the pointer pointing to the shorter line
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
                
        return max_water