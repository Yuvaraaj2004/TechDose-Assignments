class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        s1, s2 = set(), set()
        for i in nums:
            if i not in s1:
                s1.add(i)
            elif i not in s2:
                s2.add(i)
            else:
                s1.discard(i)
                s2.discard(i)
        return [i for i in s1][0]
