class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        elif n == 1:
            return [0, 1]
        dp = [-1]*(n+1)
        dp[0], dp[1] = 0, 1
        for i in range(2, n+1):
            dp[i] = (dp[i >> 1]+(i & 1) if i & (i-1) else 1)
        return dp

        '''def countbits(n):
            print()
            s=0
            while n>0:
                s+=1
                n>>=1
            return s
        for i in range(countbits(n)):
            k=0
            for j in range(2**i,2**(i+1)):
                if j<=n:
                    l.append(l[k]+1)
                    k+=1
                else:break
        return l'''
