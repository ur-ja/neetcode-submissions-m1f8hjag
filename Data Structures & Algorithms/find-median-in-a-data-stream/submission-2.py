class MedianFinder:

    def __init__(self):
        self.left = [] # max heap
        self.right = [] # min heap 

    def addNum(self, num: int) -> None:
        if len(self.left) == 0 and len(self.right) == 0:
            heapq.heappush(self.left, -num)
        elif num > -self.left[0]:
            heapq.heappush(self.right, num)
        else:
            heapq.heappush(self.left, -num)

        if len(self.left) - len(self.right) > 1:
            val = heapq.heappop(self.left)
            heapq.heappush(self.right, val)
        elif len(self.right) - len(self.left) > 1:
            val = heapq.heappop(self.right)
            heapq.heappush(self.left, val)

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (self.right[0] - self.left[0]) / 2
        elif len(self.left) > len(self.right):
            return -self.left[0]
        else:
            return self.right[0]