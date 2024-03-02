class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1

        res = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            
            if abs(nums[l]) > abs(nums[r]):
                square = nums[l]
                l += 1
            else:
                square = nums[r]
                r -= 1
            res[i] = square * square
        return res