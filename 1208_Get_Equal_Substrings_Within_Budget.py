class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        abs_diff = []
        for i in range(len(s)):
            abs_diff.append(abs(ord(s[i]) - ord(t[i])))
        
        curSum = 0
        start = 0
        maxLength = 0
        for i in range(len(abs_diff)):
            curSum += abs_diff[i]
            while curSum > maxCost:
                curSum -= abs_diff[start]
                start += 1
            maxLength = max(maxLength, i - start + 1)

        return maxLength