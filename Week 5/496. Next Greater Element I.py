class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack1 = []
        stack = []
        d = {}
        for num in nums2:
            while len(stack) and (stack[-1]<num):
                d[stack.pop()] = num
            stack.append(num)
        for num in nums1:
            stack1.append(d.get(num,-1))
        return stack1