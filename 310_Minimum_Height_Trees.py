class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]  # If there's only one node, that's the root.

        # Build the graph as an adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Use a set to keep track of the leaf nodes
        leaves = []
        for i in range(n):
            if len(graph[i]) == 1:  # A leaf has only one connection
                leaves.append(i)

        remaining_nodes = n
        # Trim the leaves until we reach the centroids
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            new_leaves = []

            for leaf in leaves:
                # Since it's a leaf, it has only one neighbor
                neighbor = graph[leaf][0]
                # Remove the leaf from its neighbor's list
                graph[neighbor].remove(leaf)

                # If the neighbor becomes a leaf, add it to new_leaves
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)

            leaves = new_leaves  # Update the leaves for the next iteration

        return leaves  # These are the centroids/minimum height tree roots

# class Solution:
#     def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
#         if n == 1:
#             return [0]

#         # Build the graph as an adjacency list
#         graph = defaultdict(list)
#         for u, v in edges:
#             graph[u].append(v)
#             graph[v].append(u)

#         # Helper function for DFS
#         def dfs(node, parent):
#             height = 0
#             for neighbor in graph[node]:
#                 if neighbor != parent:  # Avoid going back to the parent node
#                     height = max(height, 1 + dfs(neighbor, node))
#             return height

#         # Initialize a list to store heights for each root
#         heights = []

#         # Loop through all nodes and find the height when rooted at that node
#         for i in range(n):
#             heights.append((i, dfs(i, -1)))  # -1 as a non-existent parent
#         # print(heights)

#         # Find the minimum height
#         min_height = min(heights, key = lambda x: x[1])[1]

#         # Collect all nodes with the minimum height
#         min_height_roots = [node for node, height in heights if height == min_height]

#         return min_height_roots