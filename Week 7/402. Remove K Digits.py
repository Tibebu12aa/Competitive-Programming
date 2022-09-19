class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        stack = []
        for entry in num:
        # The monotonic property can only break if and only if the container
        # is not empty and the last item, compared to the entry, breaks
        # the property. While that is true, we pop the top item.
            while k>0 and stack and stack[-1] > entry:
                k-=1
                stack.pop()
                # Do something with the popped item here
            stack.append(entry)
        stack=stack[:len(stack)-k]
        res= "".join(stack)
        
        return str(int(res)) if res else "0"
    