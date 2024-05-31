class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # editorial solution
        hashmap = Counter(nums)
        return [x for x in hashmap if hashmap[x] == 1]

        # my solution
        cntMap = defaultdict(int)
        for i in range(len(nums)):
            cntMap[nums[i]] += 1
        
        ans = []
        for num, cnt in cntMap.items():
            if cnt == 1:
                ans.append(num)

        return ans