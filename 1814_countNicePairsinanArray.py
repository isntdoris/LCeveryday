class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        
        def rev(num):
            res = 0
            while num: 
                res = res * 10 + num % 10
                num //= 10
            return res

        arr = []

        for i in range(len(nums)):
            arr.append(nums[i] - rev(nums[i]))
        
        hashMap = defaultdict(int)
        ans = 0
        MOD = 10 ** 9 + 7
        for num in arr:
            ans = (ans + hashMap[num]) % MOD
            hashMap[num] += 1
        return ans