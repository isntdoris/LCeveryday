class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = right = 0
        num_zero = 1

        for right in range(len(nums)):

            if nums[right] == 0:
                num_zero -= 1
            
            if num_zero < 0:
                if nums[left] == 0:
                    num_zero += 1
                left += 1
        return right - left

