class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] == '+':
                stack.append(stack.pop() + stack.pop())
            elif tokens[i] == '*':
                stack.append(stack.pop()*stack.pop())
            elif tokens[i] == '-':
                l , r = stack.pop(),stack.pop()
                stack.append(r-l)
            elif tokens[i] == '/':
                l , r = stack.pop(),stack.pop()
                stack.append(int(r/l))
            else:
                stack.append(int(tokens[i]))
        return stack[-1]