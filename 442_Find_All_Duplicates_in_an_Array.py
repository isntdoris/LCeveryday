class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # all positive int

        ans = []
        for num in nums:
            at_index = nums[abs(num) - 1]
            if at_index < 0:
                ans.append(abs(num))
            else:
                nums[abs(num) - 1] *= -1
        return ans