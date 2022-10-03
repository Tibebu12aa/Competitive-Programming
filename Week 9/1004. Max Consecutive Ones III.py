class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        zero_idx = {i:-1 for i in range(-k, 1)}
        print(zero_idx)
        ans, zeros = 0, 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
                zero_idx[zeros] = i
               
            ans = max(ans, i - zero_idx[zeros - k])
        return ans   