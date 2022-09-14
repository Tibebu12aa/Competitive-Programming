class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # first we sort the citations list
        citations.sort()
        # then we initialize both h and n
        h,n= 1, len(citations)
        # so now we start a loop that continues to upgrade h to the end of the list
        while h<=n:
            # now if h is less than the n-h index the h-1 is the h-index
            if citations[n-h]<h:
                break
            h+=1
        return h-1