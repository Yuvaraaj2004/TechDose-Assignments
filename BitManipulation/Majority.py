class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        def BoyerMoore():
            ele, vot = -1, 0
            for i in nums:
                if vot == 0:
                    ele = i
                    vot += 1
                else:
                    if i == ele:
                        vot += 1
                    else:
                        vot -= 1
            count = 0
            for i in nums:
                if i == ele:
                    count += 1
            return (ele if count >= len(nums)//2 else -1)
        return BoyerMoore()
