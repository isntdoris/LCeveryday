class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        def dfs(curr):
            visited.add(curr)
            for key in rooms[curr]:
                if key not in visited:
                    dfs(key)
        visited = set()
        dfs(0)
        return len(visited) == len(rooms)