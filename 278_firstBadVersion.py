# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
class Solution:
    def firstBadVersion(self, n: int) -> int:
        low, high = 1, n
        # mid = (high+low) // 2

        while low <= high:
            mid = (high+low) // 2
            if isBadVersion(mid):
                if isBadVersion(mid-1):
                    high = mid - 1
                else:
                    return mid

            else:
                if isBadVersion(mid+1):
                    return mid + 1
                else:
                    low = mid + 1
        
            # mid = (high+low) // 2
        return -1