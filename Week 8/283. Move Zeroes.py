class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=0
        r=len(nums)
        for l in range(len(nums)):
            if nums==[0]:
                return [0]
            elif nums[l]==0:
                nums.insert(r,nums[l])
                nums.remove(nums[l])
        return nums