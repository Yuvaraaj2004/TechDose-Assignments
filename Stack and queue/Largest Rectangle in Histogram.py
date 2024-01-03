class Solution:
    def largestRectangleArea(self, height: List[int]) -> int:
        def Form(l, r, c):
            arr, stack = [], []
            for i in range(l, r, c):
                if not stack:
                    stack.append(i)
                    arr.append(-1)
                else:
                    while stack and height[stack[-1]] >= height[i]:
                        stack.pop()
                    arr.append(-1 if not stack else stack[-1])
                    stack.append(i)
                # print(stack)
            return arr if c == 1 else arr[::-1]
        left, right, a = Form(0, len(height), 1), Form(
            len(height)-1, -1, -1), 0
        # print(left)
        # print(right)

        def getVal(ind, left, right):
            return (len(height) if right == -1 else right)-(0 if left == -1 else left+1)
        for i in range(len(height)):
            a = max(a, height[i]*(getVal(i, left[i], right[i])))
            # print(getVal(i,left[i],right[i]))

        return a
