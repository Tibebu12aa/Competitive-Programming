class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        l=0
        r=len(nums)-1
        ans=[]
        while r>l:
            ans.append(nums[r]+nums[l])
            r-=1
            l+=1
        ans.sort()
        return ans[-1]

       