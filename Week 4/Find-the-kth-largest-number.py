class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        # we need to sort first we need to sort the list 
        # i used the buil in sort functions anda also key int 
        nums.sort(key= int)
        # now the Kth largest element is the number of elements i nums minus k
        return nums[len(nums)-k]
        