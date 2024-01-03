class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        # return True if target in nums else False
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                l,r=i+1,i
        nums=nums[l:]+nums[:l]
        l,r=0,len(nums)
        while l<r:
            mid=(l+r)//2
            if nums[mid]>target:
                r=mid-1
            elif nums[mid]<target:
                l=mid+1
            else:
                return True
        return False
