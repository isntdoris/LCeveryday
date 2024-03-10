class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # bfs
        rows = len(maze)
        cols = len(maze[0])
        q = deque()
        visited = set()
        q.append((entrance[0], entrance[1]))
        length = 0

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if (r, c) != (entrance[0], entrance[1]) and (r in [0, rows - 1] or c in [0, cols - 1]):
                    return length

                directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
                for dr, dc in directions:
                    row = r + dr
                    col = c + dc
                    if min(row, col) < 0 or row >= rows or col >= cols or maze[row][col] == '+' or (row, col) in visited:
                        continue
                    visited.add((row, col))
                    q.append((row, col))
            length += 1
        return -1