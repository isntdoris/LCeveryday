class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        ans = 0

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] != 0 and row > 0:
                    matrix[row][col] += matrix[row - 1][col]
            
            curr_row = sorted(matrix[row], reverse = True)
            for i in range(cols):
                ans = max(ans, curr_row[i] * (i + 1))
        return ans