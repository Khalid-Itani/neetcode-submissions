class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        # 1) Binary search to find the candidate row
        top, bot = 0, rows - 1
        
        while top <= bot:
            mid = (top + bot) // 2
            first = matrix[mid][0]
            last = matrix[mid][cols - 1]

            if target < first:
                bot = mid - 1
            elif target > last:
                top = mid + 1
            else:
                row = mid
                break
        
        if not top <= bot:
            return False
        
        l, r = 0, len(matrix[0]) - 1

        while l <= r:
            m = (r + l) // 2

            if matrix[row][m] < target:
                l = m + 1
            elif matrix[row][m] > target:
                r = m - 1
            else:
                return True
        return False

