class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        import collections
        # First lets create a hashtable of each value and there frequency
        # and for this we use the built in counter function 
        c=collections.Counter(nums)
        for i,v in c.items():
            #now if the frequency greater than one reeturn the value
            if v>1:
                return i