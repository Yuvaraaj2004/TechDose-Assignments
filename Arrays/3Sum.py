class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        s = set()
        for i in range(len(nums)):
            j, k = i+1, len(nums)-1
            while j < k:
                if nums[i]+nums[j]+nums[k] > 0:
                    k -= 1
                elif nums[i]+nums[j]+nums[k] < 0:
                    j += 1
                else:
                    s.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
        return s
