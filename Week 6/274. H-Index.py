class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        i,n = 1,len(citations)
        while i<=n:
            if citations[n-i]<i: 
                break
            i+=1
        return i-1