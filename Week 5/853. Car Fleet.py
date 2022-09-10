class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # first lets create a map of each vehicle with a pair of speed and position 
        maps= [[p,s] for p, s in zip(position, speed)]
        # we create now we create un empty stack which will store the fleets
        stack=[]    
        # starting from reverse sorted oreder
        for p,s in sorted(maps)[::-1]:
            #the time it takes for a  vehicle to reach the target can be calcluated
            time=(target-p)/s 
            stack.append(time)
            """
            now becausse tey are sorted in postion order if the car closest to the target
            can reach the target the fastest it will reach the target alone make a fleet by it self
            else if a vehicle behind it can reach the target the fastest then they will
            get to the target together making one fleet
            else the vehicle will not catch up and make a fleet by it self
            """  
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                """
                so each time a car behind catchs up to the current vehicle the current
                and the one behind become one 
                """
                stack.pop()
        return len(stack)