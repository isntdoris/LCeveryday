class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) < 2:
            return len(chars)
        
        i = j = 0

        while j < len(chars):
            cnt = 1
            while (j < len(chars) - 1) and (chars[j] == chars[j + 1]):
                j += 1
                cnt += 1

            chars[i] = chars[j]
            i += 1

            if cnt > 1:
                for val in str(cnt):
                    chars[i] = val
                    i += 1
            j += 1

        return i  