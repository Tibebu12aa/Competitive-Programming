class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # create two pointers 
        l,r=0,0
        prefixsum=0
        res=0
        # loop through the arrays using a slinding window 
        while r<len(arr):
            prefixsum+=arr[r]
            # while r-l+1 is less than k just move the right pointer by 1  and each time calcluate the prefix sum
            if r-l+1 <k:
                r+=1
            # when r-l+1 is equal to k first chech if this sub statisfy the second condtion
            elif r-l+1==k and (prefixsum/k) >=threshold:
                # if it does increament your res by 1 and udate points both pointers and prefix sum
                res+=1
                prefixsum-=arr[l]
                l+=1
                r+=1
            else:
                # and is it doesn just update the prefix sum and the poinyers on ly
                prefixsum-=arr[l]
                l+=1
                r+=1     
        # finally return the result
        return res