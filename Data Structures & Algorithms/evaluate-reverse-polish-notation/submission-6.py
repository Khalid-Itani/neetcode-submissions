class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []

        for i in tokens:
            if i.lstrip('-').isdigit():
                res.append(int(i))
            elif i == '+':
                solve = int(res[-2]) + int(res[-1])
                res.pop()
                res.pop()
                res.append(solve)
            elif i == '-':
                solve = int(res[-2]) - int(res[-1])
                res.pop()
                res.pop()
                res.append(solve)
            elif i == '/':
                solve = int(res[-2]) / int(res[-1])
                res.pop()
                res.pop()
                res.append(int(solve))
            elif i == '*':
                solve = int(res[-2]) * int(res[-1])
                res.pop()
                res.pop()
                res.append(solve)
        return res[-1]
