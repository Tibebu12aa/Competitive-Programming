class Solution:
     def numIdenticalPairs(self, nums: List[int]) -> int:
        #first we set our counter to Zero
        goodpairscount=0
        #then we create an empty dictionary of goodpairs
        goodpairs={}
        # after that we iterate throgh each element of the array
        for i in nums:
            # if we have encounterd that number before
            if i in goodpairs:
                #we update our coounter with the value corosponding to each number from goodpairs dictionary 
                goodpairscount+=goodpairs[i]
                #then we add 1 to the number of times we have encounterd a certain element in goodpairs dictionary
                goodpairs[i]+=1
            else:
                #if we haven't encounterd this number before we register it in the dictonary and initalize it with count 1  
                goodpairs[i]=1
        return goodpairscount 
