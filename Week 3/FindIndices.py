class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        a=[]
        for i in range(0,len(nums)):
            for j in range(0,i):
                if nums[j] >nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]

        for i in range(len(nums)):
            if nums[i] > target:
                break;
            elif nums[i] == target:
                a.append(i)
            
        return a