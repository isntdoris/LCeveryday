class Solution:
    def addBinary(self, a, b):
        result = []

        carry = 0

        i, j = len(a)-1, len(b)-1

        while i >= 0 or j >= 1 or carry:
            total = carry # this concept is critical

            if i >= 0:
                total += int(a[i])
                i -= 1

            if j >= 0:
                total += int(b[j])
                j -= 1

            result.append(str(total %2)) # using the remainder technique
            
            carry = total // 2 # dividing the sum by 2 to get the carry-over value

        return ''.join(reversed(result))
        
