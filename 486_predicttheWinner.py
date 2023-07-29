class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        visited = defaultdict(int)

        def dp(left, right, turn):
            if left > right:
                return 0
            if (left, right, turn) in visited:
                return visited[(left, right, turn)]
            
            res = 0
            if turn == 1:
                res = max(nums[left] + dp(left + 1, right, 2), nums[right] + dp(left, right - 1, 2))
            else:
                res = min(dp(left + 1, right, 1), dp(left, right - 1, 1))

            visited[(left, right, turn)] = res
            return res
        
        p1_score = dp(0, len(nums) - 1, 1)
        return sum(nums) - p1_score <= p1_score