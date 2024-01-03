class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()
        ans = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                l, r = j+1, len(nums)-1
                while l < r:
                    if nums[l]+nums[r]+nums[i]+nums[j] < target:
                        l += 1
                    elif nums[l]+nums[r]+nums[i]+nums[j] > target:
                        r -= 1
                    else:
                        ans.add((nums[l], nums[r], nums[i], nums[j]))
                        l += 1
                        r -= 1
        print(ans)
        return ans
