class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        rows, cols = len(matrix), len(matrix[0])
        ans = [[None] * rows for _ in range(cols)] # RICKY HERE
        for r in range(rows):
            for c in range(cols):
                ans[c][r] = matrix[r][c]
        return ans