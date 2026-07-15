class Solution:
    def evalRPN(self, tokens: List[str]):
        stack = []
        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                stack.append(token)
            else:
                res = 0
                operand1 = int(stack.pop())
                operand2 = int(stack.pop())
                if token == "+":
                    res = operand1 + operand2
                elif token == "*":
                    res = operand1* operand2
                elif token == "-":
                    res = operand2 - operand1
                else:
                    res = operand2/ operand1
                stack.append(res)
        return int(stack.pop())
        