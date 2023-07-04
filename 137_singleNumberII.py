class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        count = 0

        for shift in range(32):
            count = 0
            for num in nums:
                count += (num >> shift) & 1   
            count %= 3
            if count:
                res |= 1 << shift
        if res > 2**31 - 1:
            res -= 2**32
        return res

