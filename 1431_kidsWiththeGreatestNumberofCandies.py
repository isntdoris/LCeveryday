class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        tmp = candies

        for i in range(len(candies)):
            tmp[i] = tmp[i] + extraCandies

            if candies[i] != max(tmp):
                result.append(False)
            else:
                result.append(True)
            tmp[i] = tmp[i] - extraCandies
        
        return result