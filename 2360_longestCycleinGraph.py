# Approach : Depth First Search
# Here we are using a modified depth-first search algorithm to visit each node in the graph.
# We keep track of the time at which each node is visited and store it in an array called timeVisited.
# If a node is visited again, we skip it because it has already been processed.
# If the current node is visited again, and the time at which it was first visited is greater than or equal to the start time of the current traversal, it means that there is a cycle in the graph that includes the current node.
# The length of the cycle is the difference between the current time and the time at which the node was first visited.
# We also keep track of the maximum cycle length found so far and return it as the result.

class Solution:
  def longestCycle(self, edges: List[int]) -> int:
    ans = -1  # Initialize the answer to -1
    time = 1  # Initialize the current time step to 1
    timeVisited = [0] * len(edges)  # Initialize a list to store the time at which each node was first visited

    # Iterate through each node in the graph
    for i, edge in enumerate(edges): # 為什麼需要有edge
      if timeVisited[i]:  # If the node has already been visited, skip it
        continue
      startTime = time  # Record the start time of the current traversal
      u = i  # Initialize the current node(u) to the ith node
      # Traverse the graph until the end of the path is reached or a visited node is encountered
      while u != -1 and not timeVisited[u]:
        timeVisited[u] = time  # Record the current time step
        time += 1  # Increment time
        u = edges[u]  # Move to the next node in the path ！透過這一步驟在移動的！
      # If a cycle is found that includes the current node, update the answer
      if u != -1 and timeVisited[u] >= startTime:
        ans = max(ans, time - timeVisited[u])

    return ans  # Return the length of the longest cycle found