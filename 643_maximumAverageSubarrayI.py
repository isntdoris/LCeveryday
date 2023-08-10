class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        curSum = maxSum = sum(nums[0:k])

        for i in range(k, len(nums)):
            curSum = curSum - nums[i - k] + nums[i]
            maxSum = max(curSum, maxSum)
        return maxSum / k