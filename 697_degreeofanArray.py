class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # 1. group the elements
        d = defaultdict(list)
        for idx, value in enumerate(nums):
            d[value].append(idx)

        # 2. get the max degree
        m = max(len(v) for v in d.values())

        # 3. find shortest span for max degree
        best = len(nums)

        for v in d.values():
            best = min(best, v[-1] - v[0] + 1)
        return best
