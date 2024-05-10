class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        fra = []

        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                fra.append((arr[i] / arr[j], i, j))
        fra.sort(key = lambda x: x[0])
        return [arr[fra[k - 1][1]], arr[fra[k - 1][2]]]