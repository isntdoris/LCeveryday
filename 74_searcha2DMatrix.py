class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # sol 2:
                # if not matrix or not matrix[0]:
        #     return False
        
        high = 0
        low = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        while high <= low:
            mid_row = (high + low) // 2

            if matrix[mid_row][0] > target:
                low = mid_row - 1
            elif matrix[mid_row][-1] < target:
                high = mid_row + 1
            else:

                while left <= right:
                    mid_col = (left + right) // 2
                    if matrix[mid_row][mid_col] > target:
                        right = mid_col - 1
                    elif matrix[mid_row][mid_col] < target:
                        left = mid_col + 1
                    else:
                        return True
                return False
        
        # sol 1:
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
