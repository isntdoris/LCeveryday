class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, ttl):
            if ttl == target:
                res.append(cur.copy())
                return

            if ttl > target or i >= len(candidates):
                return
            
            cur.append(candidates[i])
            dfs(i, cur, ttl + candidates[i])
            cur.pop()
            dfs(i + 1, cur, ttl)

        dfs(0, [], 0)
        return res