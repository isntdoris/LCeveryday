class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # method 1 & 2 都不是很理解。。。
        # method 1
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

        # method 2
        low_bits = high_bits = 0
        for num in nums:
            low_bits = ~high_bits & (low_bits ^ num)
            high_bits = ~low_bits & (high_bits ^ num)
        return low_bits

