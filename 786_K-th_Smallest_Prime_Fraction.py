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