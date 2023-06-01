class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")": "(", "]": "[", "}": "{" }

        for c in s:
            if c in closeToOpen: # closing parentheses
                if stack and stack[-1] == closeToOpen[c]: # stack not empty && 
                    stack.pop()
                else:
                    return False
            else: # open parentheses
                stack.append(c)
        return True if not stack else False