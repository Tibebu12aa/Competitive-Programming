class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = n * [-1]
        nums += nums
        
        stack = []
        for i, num in enumerate(nums):
            while stack and stack[-1][1] < num:
                ans[stack.pop()[0]] = num
            if i < n: stack.append((i, num))
        
        return ans