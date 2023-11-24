class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        q = deque(piles)

        ans = 0
        while q:
            q.pop()
            ans += q.pop()
            q.popleft()
        return ans