class Solution(object):
    def xorQueries(self, arr, queries):
        m = {}
        m[-1] = 0
        x = 0
        for i in range(len(arr)):
            x ^= arr[i]
            m[i] = x
        
        ans = []
        for q in queries:
            if q[0] == q[1]: ans.append(arr[q[0]])
            else: ans.append(m[q[0] - 1] ^ m[q[1]])
        
        return ans