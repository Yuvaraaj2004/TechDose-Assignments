class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low, high = max(weights), sum(weights)

        def check(mid):
            d, w = 1, 0
            for i in weights:
                if w+i > mid:
                    w = i
                    d += 1
                else:
                    w += i
            return d
        while low <= high:
            mid = (low+high)//2
            print(low, high, mid)
            if check(mid) <= days:
                high = mid-1
            else:
                low = mid+1
        return low
