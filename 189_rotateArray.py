class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # [5,6,7,1,2,3,4]
        # [7,6,5,4,3,2,1]
        # [1,2,3,4,5,6,7], k = 3
        #  l       r
        #  0 1 2 3 4 5 6
        #  3 4 5 6 0 1 2
        k = k % len(nums)

        nums_rev = nums[::-1]
        a = nums_rev[0:k]
        b = nums_rev[k:len(nums)]
        a_rev = a[::-1]
        b_rev = b[::-1]
        nums[:] = a_rev + b_rev