class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        # what is the max score you can get while playing in one of two ways    
        # mentioned and you don't have to play all tokens and also you can play
        # in any order of tokens
        """
        # Input: tokens = [100], power = 50
        # Output: 0
        # Input: tokens = [100,200], power = 150
        # Output: 1
        # Input: tokens = [], power =0
        # output= 0
        # Input: tokens = [1,0], power=1
        # output= 2
        # Input: tokens = [100,200,300,400], power = 200
        # 100,100 score=1
        # 400,500 score=0
        # 200,300 score=1
        # 300,300 score=2
        # Output: 2
        """
        maxscore=0
        score=0
        #  sort tokens
        tokens.sort()
        #  place pointers at the start and last index
        l,r=0,len(tokens)-1
        # if the l pointer is less than the power play face up
        # play face down with the right pointer 
        # record max 
        if len(tokens)==0:
            return 0
        while r>=l:
            if power>=tokens[l]:
                power-=tokens[l]
                score +=1
                l+=1
                maxscore=max(score,maxscore)
            else:
                if maxscore < 1:
                    return 0
                else:
                    power+=tokens[r]
                    score -=1
                    r-=1
                    maxscore=max(score,maxscore)
        return maxscore
        