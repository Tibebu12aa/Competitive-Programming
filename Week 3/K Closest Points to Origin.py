class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # for this problem i learn a new python tool called Lambda
        # a Lambda Expression is basically an Anonymous Function
        # To create a lambda expression, you type the keyword """"lambda""""" 
        # followed by your inputs. Next, type a colon. Finally, enter an expression that
        # will be the return value.
        ## since i want only the closest points i wanto to sort them using the """sort"" expression
        points.sort(key = lambda k: k[0]**2 + k[1]**2)
 
        return points[:k]
