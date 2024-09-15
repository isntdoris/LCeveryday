class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # bitmask
        vowels = "aeiou"
        mask = 0
        res = 0
        mask_to_idx = {0: -1}

        for i, c in enumerate(s):
            print(mask)
            if c in vowels:
                mask = mask ^ (1 + ord(c) - ord('a')) # RICKY HERE
            if mask in mask_to_idx:
                length = i - mask_to_idx[mask] # RICKY HERE
                res = max(res, length)
            else:
                mask_to_idx[mask] = i
        return res