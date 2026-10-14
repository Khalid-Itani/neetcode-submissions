class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = 0
        for i, h in enumerate(heights):

            start = i
            while stack and h <= stack[-1][1]:
                index, height = stack.pop()
                width = i - index
                curr = height * width
                if curr > area:
                    area = curr
                start = index
            stack.append((start, h))
        #handle empty stack case
        n = len(heights)
        while stack:
            index, height = stack.pop()
            area = max(area, height * (n - index))
        return area