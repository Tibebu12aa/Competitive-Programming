class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        count = 0
        prefix = {}
        prefix[0] = 1
        for i in range(len(nums)):
            
            if nums[i] % 2 != 0:
                count += 1
            if count in prefix:
                prefix[count] += 1
            else: 
                prefix[count] = 1
        for c in prefix:
            if c - k in prefix:
                res += prefix[c] *prefix[c - k]
        return res