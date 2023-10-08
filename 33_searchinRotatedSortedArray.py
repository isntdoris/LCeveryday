class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [4,5,6,7,0,1,2]
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            
            # left portion
            if nums[l] <= nums[m]: # here "<="
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            # right portion
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return -1

# alternate
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [4,5,6,7,0,1,2]
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            
            if nums[m] > nums[r]: # RICKY LOOK HERE!
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return -1           