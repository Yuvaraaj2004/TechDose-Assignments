class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if max(nums) < 0:
            return max(nums)
        s, m = 0, 0
        for i in nums:
            if s+i < 0:
                s = 0
            else:
                s += i
                if s > m:
                    m = s
        return m
