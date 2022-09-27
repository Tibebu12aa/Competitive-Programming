class Solution:
    def threeSum(self, nums):
        """
        1. find three unique numbers that from the list such that there sum equals zero
        2. examples.
            nums=[-1,0,1,2,-1,-4]
            ans, [-1,0,1],[-1,2,-1]
            nums = [0,1,1]
            ans, = []
            nums = []
        """
        res = []
        nums.sort()
        n=len(nums)
        for a in range(n):
            b=a+1
            c=n-1
            while c>b:
                sums=nums[a]+nums[b]+nums[c]
                if sums>0:
                    c-=1
                elif sums<0:
                    b+=1
                else:
                    toappend=[nums[a],nums[b],nums[c]]
                    if toappend not in res:
                        res.append(toappend)
                    b+=1
                    c-=1
        return res