class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        def countbits(n):
            s = 0
            while n > 0:
                if n & 1:
                    s += 1
                n >>= 1
            return s
        return countbits(x ^ y)
