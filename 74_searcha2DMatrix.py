class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # https://www.youtube.com/watch?v=Ber2pi2C0j0
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS-1

        while top <= bot:
            row = (top+bot) // 2
            if target < matrix[row][-1]
                row = row + 1
            elif target > matrix[row][0]
                row = row - 1
            else:
                break
        # here
        if not (top <= bot):
            return False
        
        row = (top+bot) // 2

        L, R = 0, COLS - 1

        while L <= R:
            m = (L+R) // 2
            if target > matrix[row][m]:
                L = m + 1
            elif target < matrix[row][m]:
                R = m - 1
            else:
                return True
        return False
