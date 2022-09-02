class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        maxOperation = 0
        while left < right:
            cur = nums[left] + nums[right]
            if cur == k:
                maxOperation += 1
                left += 1
                right -= 1
            elif cur < k:
                left += 1
            else:
                right -= 1
        return maxOperation