class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # first because i want to iterate throgh all elements of a and am 
        # comparing the i-1 and i+1 terms i will execlude the first and last terms
        for i in range(1,len(nums)-1):
            # now my main goal here is to avoid any 3 consequtive elements 
            # weither they are in increasing or decreasing order
            if  nums[i-1]<nums[i]<nums[i+1] or nums[i-1]>nums[i]>nums[i+1] :
                # if there are consequtive elements then we swap elements
                nums[i],nums[i+1]=nums[i+1],nums[i]
            else: 
                #if not we pass to the next element
                pass
        return nums
                