class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n=len(arr)
        ans=0
        i=1
        while i<n-1:
            if arr[i-1]<arr[i]>arr[i+1]:
                j=i
                count=1
                while j>0 and arr[j]>arr[j-1]:
                    count+=1
                    j-=1
                k=i
                while k<n-1 and arr[k]>arr[k+1]:
                    k +=1
                    count+=1
                ans=max(ans,count)
                i+=1
            else:
                i+=1
        return ans 
        