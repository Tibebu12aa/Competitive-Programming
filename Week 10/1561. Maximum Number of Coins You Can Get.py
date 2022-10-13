class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        l=0
        ans=0
        for j in range(len(piles)-1,-1,-2):
            r=j-1
            if r>l:
                ans += piles[r]
            else:
                return ans
            l+=1

        
        return ans
             