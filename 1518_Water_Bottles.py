class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles

        while numBottles >= numExchange: # RICKY HERE
            drink = numBottles // numExchange
            remaining = numBottles % numExchange

            ans += drink
            numBottles = drink + remaining

        return ans