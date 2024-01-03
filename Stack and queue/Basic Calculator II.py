class Solution:
    def calculate(self, s: str) -> int:
        def postFix():
            stack, i = [], 0
            exp = []
            while i < len(s):
                if s[i] == ' ':
                    i += 1
                elif s[i] == '+' or s[i] == '-':
                    while stack:
                        exp.append(stack.pop())
                    stack.append(s[i])
                    i += 1
                elif s[i] == '*' or s[i] == '/':
                    while stack and stack[-1] in {'*', '/'}:
                        exp.append(stack.pop())
                    stack.append(s[i])
                    i += 1
                else:
                    ans = 0
                    while i < len(s) and s[i].isdigit():
                        ans = ans*10+int(s[i])
                        i += 1
                    exp.append(ans)
            while stack:
                exp.append(stack.pop())
            return exp

        def Eval(l):
            def Rec():
                if l[-1] in {'+', '-', '*', '/'}:
                    v = l.pop()
                    if v == '+':
                        return Rec()+Rec()
                    elif v == '-':
                        return -Rec()+Rec()
                    elif v == '*':
                        return Rec()*Rec()
                    elif v == '/':
                        return int(1/Rec()*Rec())
                else:
                    return l.pop()
            return Rec()
        return Eval(postFix())

        return 0
