class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        cnt_map = defaultdict(int)
        for num in nums:
            cnt_map[num] += 1
        max_fq = max(cnt_map.values())
        max_fq_eles = [num for num, fq in cnt_map.items() if fq == max_fq]
        return max_fq * len(max_fq_eles)