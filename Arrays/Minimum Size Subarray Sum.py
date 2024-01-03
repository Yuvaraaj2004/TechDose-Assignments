class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, s, ans = 0, 0, float('inf')
        for i in range(len(nums)):
            s += nums[i]
            while s > target:
                s -= nums[left]
                ans = min(ans, i-left+1)
                left += 1
            if s >= target:
                ans = min(ans, i-left+1)
        return ans if ans !=float('inf') else 0