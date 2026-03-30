class MedianFinder:

    def __init__(self):
        self.stream = []

    def addNum(self, num: int) -> None:
        self.stream.append(num)

    def findMedian(self) -> float:
        sorted_stream = sorted(self.stream)
        if len(sorted_stream) % 2 != 0:
            return sorted_stream[(len(sorted_stream) // 2)]
        else:
            return (sorted_stream[(len(sorted_stream) // 2)] + sorted_stream[(len(sorted_stream) // 2) - 1]) / 2
        