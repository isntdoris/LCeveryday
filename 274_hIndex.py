class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()

        for i, v in enumerate(citations):
            if len(citations) - i <= v:
                return len(citations) - i
        return 0
        
        # https://www.youtube.com/watch?v=FvnTWDKT_ck