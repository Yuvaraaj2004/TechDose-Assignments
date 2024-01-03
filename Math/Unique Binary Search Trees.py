class Solution:
    def numTrees(self, n: int) -> int:
        def combination(n, r, memo=dict()):
            if r == 0 or n == r:
                return 1
            elif n == r-1 or r == 1:
                return n
            elif (n, r) in memo.keys():
                return memo[(n, r)]
            else:
                memo[(n, r)] = combination(n-1, r-1)+combination(n-1, r)
                return memo[(n, r)]
        return combination(2*n, n)//(n+1)
