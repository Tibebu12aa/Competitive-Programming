class Solution:
    def reverseParentheses(self, s: str) -> str:
        """
        for this operation i choose to start from the inner loop so 
        first we create an empty stack
        now for every charachter in string s if the charachter is not ")" we simply append it to the stack
        else if the charcher is ")" we pop the all the elemnts behind it until we reach "(" and inorder to 
        reverse it we append them to a tmp variable  
        after that we now remove the "(" charcter which is now the last element of the stack
        now we append all the elemnts in tmp to the stack 
        finaly we print the stack as a single string by usig the join method
        """
        stack = []
        for i in s:
            if i == ')':
                tmp = ""
                while stack[-1] != '(':
                    tmp += stack.pop()
                stack.pop()
                for j in tmp: stack.append(j)
            else:
                stack.append(i)
        return "".join(stack)
            
        """
        test case
         #  ["(ed(et(oc))el)"]
        # stack=["(ed(et(oc"]
        # tmp=""
        # temp="co"
        # stack=["(ed(et]
        # stack=["(ed(etco]
        # tmp=""
        # tmp="octe"
        # stack=["(ed]
        # stack=["(edocte]
        # stack=["(edocteel]
        # temp=""
        # temp="leetcode"
        # stack=[""]
        # stack=["leetcode"]
        return = leetcode
        """