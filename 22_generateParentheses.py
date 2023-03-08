# 1. The idea is to add ')' only after valid '('
# 2. We use two integer variables left & right to see how many '(' & ')' are in the current string
# 3 .If left < n then we can add '(' to the current string
# 4. If right < left then we can add ')' to the current string

# **need to think about how to make sure to add ')' only after valid '('**

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(left, right, s):
            if len(s) == n * 2:
                res.append(s)
                return 

            if left < n: # Does this mean that it will always start from (1, 0, '(')? Ans: Yes, I think so..
                dfs(left + 1, right, s + '(')

            if right < left:
                dfs(left, right + 1, s + ')')

        res = [] # initiate in the beginning reduces the efficiency somehow
        dfs(0, 0, '')
        return res