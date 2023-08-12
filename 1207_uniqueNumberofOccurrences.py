class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cntMap = {}
        for ele in arr:
            if ele not in cntMap:
                cntMap[ele] = 1
            else:
                cntMap[ele] += 1
        
        if len(set(cntMap.values())) == len(set(arr)):
            return True
        return False