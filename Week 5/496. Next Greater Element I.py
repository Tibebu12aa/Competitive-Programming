class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # first lets create a hashmap conrtaining all the values and there index of num1
        d={n:i for i,n in enumerate(nums1)}
        """
        trying to simplfy our code lets lets set all the elements in final result to -1 
        and we will update each specific index later if it has a next greater element
        """
        result=[-1]* len(nums1)
        # for each value in nums2 if it does't exit in nums1 we will proced to the i+1 element
        for i in range(len(nums2)):
            if nums2[i] not in d:
                continue
            #else if it exists we find the next element then
            for j in range(i+1, len(nums2)):
                if nums2[j]>nums2[i]:
                    """
                         after finding the next element we want to put it on the correct index coresponding                          to the nums1   value so we look it up on the hashmap
                    """
                    index_1=d[nums2[i]]
                    # finally we update the result at the correct index 
                    result[index_1]=nums2[j]
                    # we use the break function here because we want to first next value
                    break
        return result