# 1. BFS to traverse the graph
# 2. A hash map to keep track of already visited and already cloned nodes

# We push a node in the queue and make sure that the node is already cloned.
# Then we process neighbors. If a neighbor is already cloned and visited,
# we just append it to the current clone neighbors list,
# otherwise, we clone it first and append it to the queue to make sure that we can visit it in the next tick.

class Solution 1:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node
        
        q, clones = deque([node]), {node.val: Node(node.val, [])}
        while q:
            cur = q.popleft() 
            cur_clone = clones[cur.val]            

            for ngbr in cur.neighbors:
                if ngbr.val not in clones:
                    clones[ngbr.val] = Node(ngbr.val, [])
                    q.append(ngbr)
                    
                cur_clone.neighbors.append(clones[ngbr.val])
                
        return clones[node.val]


class Solution 2:    
    def cloneGraph(self, node):
        if not node:
            return None

        visited = {}
        queue = deque([node])

        # Create a copy of the starting node and add it to visited
        visited[node] = Node(node.val)

        while queue:
            # Get the next node from the queue
            curr_node = queue.popleft()

            # Loop through the current node's neighbors
            for neighbor in curr_node.neighbors:
                if neighbor not in visited:
                    # Create a copy of the neighbor and add it to visited
                    visited[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                # Add the copy of the neighbor to the copy of the current node's neighbors
                visited[curr_node].neighbors.append(visited[neighbor])

        return visited[node]