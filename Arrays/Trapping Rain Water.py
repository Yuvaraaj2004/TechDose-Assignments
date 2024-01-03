class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        lmax, rmax = height[l], height[r]
        c = 0
        for i in range(1, len(height)):
            if lmax < rmax:
                l += 1
                if lmax-height[l] < 0:
                    lmax = max(height[l], lmax)
                else:
                    c += (lmax-height[l])
            else:
                r -= 1
                if rmax-height[r] < 0:
                    rmax = max(height[r], rmax)
                else:
                    c += (rmax-height[r])
        return c
