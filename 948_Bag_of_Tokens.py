class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        
        tokens.sort()
        res = score = 0
        l, r = 0, len(tokens) - 1

        while l <= r: # RICKY HERE
            if power >= tokens[l]:
                power -= tokens[l]
                score += 1
                l += 1
                res = max(res, score) # [50,50,50,100,100]
            elif score > 0:
                score -= 1
                power += tokens[r]
                r -= 1
            else:
                break
        return res 