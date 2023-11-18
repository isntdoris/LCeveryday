class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {} # {num: index}

        for index, num in enumerate(nums):
            diff = target - num
            if diff in hashMap:
                return [hashMap[diff], index]
            hashMap[num] = index