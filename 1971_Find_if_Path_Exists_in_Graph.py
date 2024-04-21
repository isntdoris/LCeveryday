class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # print(graph)

        def dfs(node, visited):
            if node == destination:
                return True
            visited.add(node)

            for neighbor in graph[node]:
                # print(node, neighbor)
                # print('zzz')
                if neighbor not in visited:
                    
                    # RICKY HERE
                    if dfs(neighbor, visited):
                        return True
            return False
        
        visited = set()
        return dfs(source, visited)