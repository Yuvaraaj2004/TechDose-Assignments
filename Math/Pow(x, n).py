class Solution:

    def myPow(self, x: float, n: int) -> float:
        def Pow(b=x, p=n):
            if p == 0:
                return 1
            return (b if p & 1 else 1)*Pow(b*b, p >> 1)

        return 1 if n ==0 else (Pow() if n>0 else 1/Pow(x,-n))