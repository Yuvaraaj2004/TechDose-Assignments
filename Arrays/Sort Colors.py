class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = [0]*3
        for i in nums:
            l[i] += 1
        for i in range(1, 3):
            l[i] += l[i-1]
        for i in nums[::]:

            nums[l[i]-1] = i
            l[i] -= 1
