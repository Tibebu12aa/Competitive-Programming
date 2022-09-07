class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        size = len(nums)
        nums+=nums
        final = [-1] * size
        stack = []
        for i in list(range(size))*2:
            while stack and (nums[stack[-1]] < nums[i]):
                final[stack.pop()] = nums[i]
            stack.append(i)
        return final