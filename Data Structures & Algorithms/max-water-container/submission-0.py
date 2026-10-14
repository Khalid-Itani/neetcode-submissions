class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) - 1

        curr = 0
        largest = 0

        while start < end:
            curr = (end - start) * min(heights[start], heights[end])
            if curr > largest:
                largest = curr
            
            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1
            
        return largest