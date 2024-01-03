class Solution:
    def countPrimes(self, n: int) -> int:
        c, v = 0, sqrt(n)+1
        s = set()
        for i in range(2, n):
            if i not in s:
                c += 1
                if i < v:
                    for j in range(i**2, n, i):
                        s.add(j)
        return c
