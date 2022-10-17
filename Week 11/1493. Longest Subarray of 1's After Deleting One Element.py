class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # first create the object to returned 
        res=0
        # set two pointers that are going to be egdes of sliding window
        l,r=0,0
        # create annobject that will tell me if i have deleted a zero before
        tempo=0
        last=0
        lastindex=0
        # loop through all the elements in array
        while r<len(nums):
            # while the element i in counter is a one just increase my riight pointer
            if nums[r]==1 and last==0 and r==len(nums)-1:
                return res
            # else if the element is a zero first check if we have deleted a zero before
            elif nums[r]==1:
                tempo+=1
            elif nums[r]==0 and last==0:
                last=1
                last_index=r
            # if we did delete a zero before while our left pointer reachs the irst zero increamnet the left pointer 
            elif nums[r]==0 and last==1:
                tempo-=(last_index-l)
                l=last_index+1
                last_index=r
            # each time update result 
            res=max(res,tempo)
            r+=1
        # return res
        return res
       