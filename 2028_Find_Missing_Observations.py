class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)

        subttl = sum(rolls)
        gap = mean * (m + n) - subttl
        if n * 6 < gap or gap < n: # RICKY HERE
            return []
        
        distribute_mean = gap // n
        mod = gap % n

        ans = [distribute_mean] * n
        for i in range(mod): # RICKY HERE
            ans[i] += 1
        return ans