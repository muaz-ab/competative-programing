class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        count , res = 0 , 0
        for i in s:
            if i == '(':
                stack.append(0)

            elif i ==')':
                temp = stack.pop()
                if temp == 0:
                    count = 1
                else:
                    count = temp*2
                if stack:
                    stack[-1] += count
                else:
                    res += count
        return res
            
