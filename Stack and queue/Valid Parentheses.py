class Solution:
    def isValid(self, s: str) -> bool:
        if (len(s) % 2 or s[0] in [')', '}', ']']):
            return False
        l = []

        for i in s:
            if i in ['[', '{', '(']:
                l.append(i)
            elif i == ']' and len(l) > 0 and l[-1] == '[':
                l.pop(-1)
            elif i == ')' and len(l) > 0 and l[-1] == '(':
                l.pop(-1)
            elif i == '}' and len(l) > 0 and l[-1] == '{':
                l.pop(-1)
            else:
                return False
        return True if len(l) == 0 else False
