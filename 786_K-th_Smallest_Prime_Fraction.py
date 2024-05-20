# Input: arr = [1,2,3,5], k = 3
# Output: [2,5]
# how to sort in less than O(n^2)
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        fra = []

        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                fra.append((arr[i] / arr[j], i, j))
        fra.sort(key = lambda x: x[0])
        return [arr[fra[k - 1][1]], arr[fra[k - 1][2]]]

class Solution:
    def kthSmallestPrimeFraction(self, arr, k):
        # Create a priority queue to store pairs of fractions
        pq = []
        # Custom comparator for priority queue
        def compare(a, b):
            return a[0] - b[0]
        # Push the fractions formed by dividing each element by
        # the largest element into the priority queue
        for i in range(len(arr)):
            heapq.heappush(pq, ((arr[i] / arr[-1]), i, len(arr) - 1))
        # Iteratively remove the top element (smallest fraction) 
        # and replace it with the next smallest fraction
        for _ in range(k - 1):
            cur = heapq.heappop(pq)
            numerator_index = cur[1]
            denominator_index = cur[2] - 1
            if denominator_index > numerator_index:
                heapq.heappush(pq, (
                    (arr[numerator_index] / arr[denominator_index]), 
                    numerator_index, 
                    denominator_index
                ))
        # Retrieve the kth smallest fraction from 
        # the top of the priority queue
        result = heapq.heappop(pq)
        return [arr[result[1]], arr[result[2]]]