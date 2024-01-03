class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ma = 0
        mx = 0
        # if prices==sorted(prices)[::-1]:return 0
        for i in range(len(prices)-1, -1, -1):
            if prices[i] > ma:
                ma = prices[i]
            else:
                mx = max(mx, ma-prices[i])
            print(ma, mx)
        return mx
