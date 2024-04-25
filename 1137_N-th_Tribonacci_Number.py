class Solution:
    def tribonacci(self, n: int) -> int:
        memo = defaultdict(int)

        memo[0], memo[1], memo[2] = 0, 1, 1

        def dp(n):
            if n in memo:
                return memo[n]
            memo[n] = dp(n - 3) + dp(n - 2) + dp(n - 1)
            return memo[n]

        return dp(n)