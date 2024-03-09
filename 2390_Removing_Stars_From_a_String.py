class Solution:
    def removeStars(self, s: str) -> str:
        res = []

        for ele in s:
            if ele != '*':
                res.append(ele)
            else:
                res.pop()
            
        return ''.join(res)
# time: O(n)
# space: O(n)