class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []

        for i in tokens:
            if i == '+':
                res.append(res.pop() + res.pop())
            elif i == '-':
                a, b = res.pop(), res.pop()
                res.append(b - a)
            elif i == '/':
                a, b = res.pop(), res.pop()
                res.append(int(b / a))
            elif i == '*':
                solve = int(res[-2]) * int(res[-1])
                res.pop()
                res.pop()
                res.append(solve)
            else:
                res.append(int(i))
        return res[-1]
