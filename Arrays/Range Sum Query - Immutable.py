
class NumArray:

    def __init__(self, nums: List[int]):
        self.array = [nums[0]]
        for i in range(1, len(nums)):
            self.array.append(self.array[-1]+nums[i])
        print(self.array)

    def sumRange(self, left: int, right: int) -> int:
        return self.array[right]-(self.array[left-1] if left-1 >= 0 else 0)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
