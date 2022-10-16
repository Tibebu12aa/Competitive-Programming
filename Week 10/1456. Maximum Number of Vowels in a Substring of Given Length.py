class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # create the to be returnd 
        res=0
        # create our vouls librabry
        vowels=["a","e","i","o","u"]
        # create two pointers 
        l,r=0,0
        prefix=0
        # loop throgh the s charcters 
        while r<len(s):
            if s[r] in vowels:
                prefix+=1
            # while our winow span is less than k each check wetheer s[r] is a vowel or not and if it is increment your prefixsum
            if r-l+1<k:
                # update r+=1
                r+=1
            # when  our window span reachs k
            else:
                # ?update our rsul an before updating the left pointer chechkk if the left element is vowwrl
                res=max(prefix,res)
                if s[l] in vowels:
                    prefix-=1
                #  if it is prefix sum is going to be decremented
                l+=1
                r+=1
        # return the result 
        return res