class Solution:
    def minSpeedOnTime(self, dist, hour):
        def can_make_it(speed):
            time = 0
            for d in dist:
                time = math.ceil(time)
                time += d/speed
            return 1 if time <= hour else -1
        
        res = float('inf')
        left, right = 1, 10**7

        while left <= right:
            pivot = (left + right) // 2
            if can_make_it(pivot) == 1:
                res = min(res, pivot)
                right = pivot - 1
            else:
                left = pivot + 1
        return res if res != float('inf') else -1
