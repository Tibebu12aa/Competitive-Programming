class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        #first create an array with equal number of elements as nums and all counts are 0
        count=[0 for x in range(len(nums))]
        #now start an outer loop so that the program runs for every element of nums  
        for i in range(0,len(nums)):
            #another inner loop to compare the j to other elemnts
            for j in nums:
                #the condtion we want to be 
                if nums[i] > j:
                    #each time the condtion is satisfied increase the count by one 
                    count[i]+=1
        return count