class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        ans = 0
        hashMap = defaultdict(int)

        for num in nums:
            ans = ans + hashMap[num]
            hashMap[num] += 1
        return ans