class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        top, bot = 0, ROWS - 1

        while top <= bot:
            m = (top + bot) // 2
            first = matrix[m][0]
            last = matrix[m][COLS - 1]

            if target < first:
                bot = m - 1
            elif target > last:
                top = m + 1
            else:
                row = m
                break
        
        if not top <= bot:
            return False
        
        l, r = 0, len(matrix[0]) - 1

        while l <= r:
            m = (l + r) // 2
            
            if matrix[row][m] < target:
                l = m + 1
            elif matrix[row][m] > target:
                r = m - 1
            else:
                return True
        return False
        