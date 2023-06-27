class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 方法一（可以理解！
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l+r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)
            
            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res

        # 方法二（曾經可以理解
        # Define the search space
        left = 1
        right = max(piles)

        # Define a function to check if it's possible to eat all bananas in h hours
        def can_eat_all_bananas(speed): # speed from mid pointer
            time = 0
            for pile in piles:
                time += (pile + speed - 1) // speed # to determine how much time to put into "time" because if pile is less than k, it still takes 1 hour that's why we are adding numerator k here
            return time <= h

        # Binary search for the minimum speed
        while left < right:
            mid = (left + right) // 2
            if can_eat_all_bananas(mid): # call function as condition to move pointers
                right = mid
            else:
                left = mid + 1

        return left # 不懂為什麼return left