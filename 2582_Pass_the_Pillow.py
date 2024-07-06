class Solution:
    def passThePillow(self, n: int, time: int) -> int:

        rounds = time // (n - 1)
        remaining = time % (n - 1)
        
        if rounds % 2 == 0:
            return remaining + 1
        else:
            return n - remaining