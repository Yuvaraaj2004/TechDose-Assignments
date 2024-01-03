class MedianFinder:

    def __init__(self):
        from sortedcontainers import SortedList
        self.c = 0
        self.prefix = SortedList()

    def addNum(self, num: int) -> None:
        self.prefix.add(num)
        self.c += 1

    def findMedian(self) -> float:
        if len(self.prefix) % 2:
            return self.prefix[len(self.prefix)//2]
        else:
            return (self.prefix[len(self.prefix)//2]+self.prefix[len(self.prefix)//2-1])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
