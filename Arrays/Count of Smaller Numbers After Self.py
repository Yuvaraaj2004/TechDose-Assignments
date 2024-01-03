class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        nums = [(nums[i], i) for i in range(len(nums)-1, -1, -1)]
        res = [0]*len(nums)

        def Merge(l=0, r=len(nums)-1):
            if l >= r:
                return
            m = (l+r)//2

            Merge(l, m)
            Merge(m+1, r)

            i = l
            for j in range(m+1, r+1):
                while i < m+1 and nums[i][0] < nums[j][0]:
                    i += 1
                res[nums[j][1]] += i-l
            nums[l:r+1] = sorted(nums[l:r+1])

        Merge()
        return res
