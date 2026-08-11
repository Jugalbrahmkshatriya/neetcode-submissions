class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # Stores indices
        max_area = 0
        heights.append(0)  # Sentinel bar to clear the stack at the end
        
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
            
        heights.pop()  # Clean up the modified input
        return max_area