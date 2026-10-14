class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) - 1
        largest = 0

        while start < end:
            curr = (end - start) * min(heights[start], heights[end])
            largest = max(curr, largest)
            
            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1
            
        return largest