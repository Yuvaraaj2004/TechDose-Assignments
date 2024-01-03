class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastpeak = -1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                lastpeak = i
        if lastpeak == -1:
            i, j = 0, len(nums)-1
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        else:
            ind = lastpeak
            for i in range(lastpeak, len(nums)):
                if nums[i] > nums[lastpeak-1] and nums[i] < nums[ind]:
                    ind = i
            nums[lastpeak-1], nums[ind] = nums[ind], nums[lastpeak-1]
            print(nums, lastpeak-1, ind)
            for ind, i in enumerate(nums[:lastpeak]+sorted(nums[lastpeak:])):
                nums[ind] = i
