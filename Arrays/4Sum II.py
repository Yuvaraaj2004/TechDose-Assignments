class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        s = {}
        for i in nums1:
            for j in nums2:
                s[i+j] = s.get(i+j, 0)+1
        ans = 0
        for i in nums3:
            for j in nums4:
                if s.get(-i-j, None):
                    ans += s[-i-j]
        return ans
