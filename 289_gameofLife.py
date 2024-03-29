class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # original | new | state
        #    0        0      0
        #    1        0      1
        #    0        1      2
        #    1        1      3

        ROWS = len(board)
        COLS = len(board[0])

        def countNeighbors(r, c):
            nei = 0
            for i in range(r - 1, r + 2):
                for j in range(c - 1, c + 2):
                    if ((i == r and j == c) or i < 0 or j < 0 or i == ROWS or j == COLS):
                        continue
                    # print(r, c)
                    # print(i, j)
                    # print('zzz')
                    # print(board[i][j])
                    if board[i][j] in [1, 3]: # 為什麼可以提前判斷3的情境。。。想不通
                        # print(board[i][j])
                    # if board[i][j] == 1:
                        nei += 1
            return nei
        print(board)

        for r in range(ROWS):
            for c in range(COLS):
                nei = countNeighbors(r, c)
                if board[r][c]: # check original == 1 and nei in [2,3]
                    if nei in [2, 3]:
                        board[r][c] = 3
                elif nei == 3: # check original == 0 and nei == 3
                    board[r][c] = 2
        # print(board)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 1:
                    board[r][c] = 0
                if board[r][c] in [2, 3]:
                    board[r][c] = 1
        # board[r][c]
        # board[r - 1][c - 1]
        # board[r - 1][c]
        # board[r - 1][c + 1]
        # board[r][c - 1]
        # board[r - 1][c + 1]
        # board[r + 1][c - 1]
        # board[r + 1][c]
        # board[r + 1][c + 1]