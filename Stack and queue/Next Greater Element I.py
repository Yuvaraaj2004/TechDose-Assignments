class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d, stack = {}, []
        for i in range(len(nums2)-1, -1, -1):
            while stack and stack[-1] < nums2[i]:
                stack.pop()
            d[nums2[i]] = -1 if not stack else stack[-1]
            stack.append(nums2[i])
        for i in range(len(nums1)):
            nums1[i] = d[nums1[i]]
        return nums1
