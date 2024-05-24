class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        
        def helper(i, cntMap):

            if i == len(nums):
                return 1
            
            # skip nums[i]
            res = helper(i + 1, cntMap)
            # include nums[i]
            if not cntMap[nums[i] - k] and not cntMap[nums[i] + k]:
                cntMap[nums[i]] += 1
                res += helper(i + 1, cntMap)
                cntMap[nums[i]] -= 1
            return res
        
        return helper(0, defaultdict(int)) - 1