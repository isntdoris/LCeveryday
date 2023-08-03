class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phone = {2: "abc", 
                 3: "def",
                 4: "ghi",
                 5: "jkl",
                 6: "mno",
                 7: "pqrs",
                 8: "tuv",
                 9: "wxyz"}

        res = []
        curr = []
        def backtrack(index):
            if index == len(digits):
                res.append(''.join(curr))
                return
            
            key = int(digits[index])
            value = phone[key]
            for i in range(len(value)):
                curr.append(value[i])
                backtrack(index + 1)
                curr.pop()
        backtrack(0)
        return res