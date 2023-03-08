# https://leetcode.com/problems/jump-game-iv/solutions/3257846/day-64-bfs-o-n-time-and-o-n-space-easiest-beginner-friendly-sol/
# 1. create an unordered_map called indices to store the indices of each value in the input array
# 2. for each value in the input array, add its index to the corresponding vector in the indices map
# 3. create a queue called storeIndex to store the indices of adjacent elements and a vector called visited to mark visited indices.
# 4. push the first index of the array to the storeIndex queue and mark it as visited int he visited vector
# 5. initialize a steps variable to 0
# 6. while the storeIndex queue is not empty, do the following:
#     6.1 get the size of the storeIndex queue
#     6.2 for each index in the storeIndex queue, do the following:
#         6.2.1 if the index is the last index of the array, return the number of steps
#         6.2.2 get the vector of indices for the current value from the indices map
#         6.2.3 add the indices of the adjacent elements to the vector
#         6.2.4 for each index in the vector, if it is within the array bounds and has not been visited, push it to the storeIndex queue and mark it as visited in the visited vector
#         6.2.5 clear the vector of indices
#     6.3 increment the steps variable
# 7. if the last index of the array is not reached, return -1

from collections import defaultdict, deque

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0
        
        indices = defaultdict(list)
        for i in range(n):
            indices[arr[i]].append(i)
        
        storeIndex = deque()
        visited = [False] * n
        storeIndex.append(0)
        visited[0] = True
        steps = 0
        
        while storeIndex:
            size = len(storeIndex)
            while size > 0:
                currIndex = storeIndex.popleft()
                size -= 1
                if currIndex == n - 1:
                    return steps
                
                jumpNextIndices = indices[arr[currIndex]]
                jumpNextIndices.append(currIndex - 1)
                jumpNextIndices.append(currIndex + 1)
                for jumpNextIndex in jumpNextIndices:
                    if 0 <= jumpNextIndex < n and not visited[jumpNextIndex]:
                        storeIndex.append(jumpNextIndex)
                        visited[jumpNextIndex] = True
                jumpNextIndices.clear()
            steps += 1
        return -1