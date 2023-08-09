class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrices = []
        curMin = prices[0]
        for i in range(len(prices)):
            curMin = min(prices[i], curMin)
            minPrices.append(curMin)
        
        curMax = 0
        for i in range(len(prices)):
            curMax = max(prices[i] - minPrices[i], curMax)
        return curMax