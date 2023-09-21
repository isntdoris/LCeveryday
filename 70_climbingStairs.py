# class Solution:
#     def climbStairs(self, n: int) -> int:
#         one, two = 1, 1
# 0, 1, 2, 3, 4
# 1, 1, 2, 3, 5

#         for i in range(n-1): # n-1
#             temp = one
#             one = one + two
#             two = temp
            
#         return one

class Solution:
    def climbStairs(self, n: int) -> int:
        #edge cases
        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 2

        dp = [0] * (n + 1) # considering zero steps we need n+1 places
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1): # n+1 (3, n+1)
            dp[i] = dp[i - 1] + dp[i - 2]
        print(dp)
        return dp[n]

        # n 0, 1, 2, 3, 4, 5
        #   0, 1, 2, 3, 5, 8
        # n 0, 1, 2, 3, 4, 5
        #   1, 2, 3, 5, 8