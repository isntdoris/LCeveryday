class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curSum = cnt = 0
        h = defaultdict(int)

        for num in nums:

            curSum += num

            if curSum == k:
                cnt += 1
            if curSum - k in h:
                cnt += h[curSum - k]

            h[curSum] += 1

        return cnt