class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        mn, mx = 1, m*n
        while mn <= mx:
            mid = (mn+mx)//2

            if sum([min(n, mid//i) for i in range(1, m+1)]) >= k:
                ans = mid
                mx = mid-1
            else:
                mn = mid+1
        return ans
