class Solution:
    def minimumLength(self, s: str) -> int:
        # 01234567
        # cabaabac
        #    lr
        l, r = 0, len(s) - 1
        while l < r and s[l] == s[r]:
            print(l, r)
            tmp = s[l] # RICKY HERE
            while l <= r and s[l] == tmp: # RICKY HERE: l <= r
                l += 1
            while l <= r and s[r] == tmp: # RICKY HERE: l <= r
                r -= 1
            print(l, r)
            print('zzz')
        return (r - l) + 1