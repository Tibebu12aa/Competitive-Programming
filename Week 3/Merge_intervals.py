class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # in order to merge the overlapping intervals firs the intervals list needs to be sorted in order using the first element as key 
	# and for that i used the sort function and lambda expression
        intervals.sort(key = lambda y: y[0])
        # now we create an empty list wich will hold the non_overlapping intervals
        non_overlapping=[]
        # now for each first element in intervals we will check if it is overlapping with the second elemnt        
        # of the previous 
        for i in intervals:
            #then if the element doesn't exist in the non_overlapping list we append
            if not non_overlapping or non_overlapping[-1][1] < i[0]:
                non_overlapping.append(i)
            else:
			#  if the current interval does not strictly dominate previous interval end, we want to merge               
            #  that interval in our list
                non_overlapping[-1][1] = max(non_overlapping[-1][1], i[1])
            
        return non_overlapping
