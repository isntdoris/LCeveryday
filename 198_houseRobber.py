class Solution:
    def rob(self, nums: List[int]) -> int:
        # from left to right
        # nums = [1, 2, 3, 1]
        #                  ^
        # robFrom(i) = max(robFrom(i + 1), robFrom(i + 2) + nums(i))
        # [rob1, rob2, n, n + 1, ...]
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp # temp (max) was assigned to rob2 at previous step
        return rob2