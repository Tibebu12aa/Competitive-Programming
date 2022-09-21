class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        days=[0]*len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd=stack.pop()
                days[stackInd]=i-stackInd
            stack.append([t,i])
        return days
        