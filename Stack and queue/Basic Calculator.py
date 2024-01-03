class Solution:
    def calculate(self, s: str) -> int:
        def postfix(s):
            print(s)
            stack, i = [], 0
            ans = []
            while i < len(s):
                if s[i] == '(':
                    stack.append('(')
                    i += 1
                elif s[i] in {'+', '-'}:

                    if i-1 < 0 or s[i-1] == '(':
                        ans.append(0)

                        stack.append(s[i])
                        i += 1
                    else:
                        if stack and stack[-1] in {'+', '-'}:
                            ans.append(stack.pop())

                        stack.append(s[i])
                        i += 1

                elif s[i] == ')':
                    while stack[-1] != '(':
                        ans.append(stack.pop())
                    stack.pop()
                    i += 1
                elif s[i] == ' ':
                    i += 1
                else:
                    num = 0
                    while i < len(s) and s[i].isdigit():
                        num = num*10+int(s[i])
                        i += 1
                    ans.append(num)
            while stack:
                ans.append(stack.pop())
            print(ans)
            return ans

        def Eval(l, ind):
            # print(l)
            val = l.pop()
            if type(val) is int:
                return val
            elif val == '+':
                return Eval(l, ind-1)+Eval(l, ind-1)
            elif val == '-':
                return -Eval(l, ind-1)+Eval(l, ind-1)

        l = postfix(''.join([i for i in s if i != ' ']))
        return Eval(l, len(l)-1)
