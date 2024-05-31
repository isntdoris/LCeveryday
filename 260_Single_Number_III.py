class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        cntMap = defaultdict(int)
        for i in range(len(nums)):
            cntMap[nums[i]] += 1
        
        ans = []
        for num, cnt in cntMap.items():
            if cnt == 1:
                ans.append(num)

        return ans