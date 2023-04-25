class SmallestInfiniteSet:

    def __init__(self):
        self.s = list(range(1,1001))

    def popSmallest(self) -> int:
        self.s.sort()
        n = self.s[0]
        self.s[:] = self.s[1:]
        return n

    def addBack(self, num: int) -> None:
        if num not in self.s:
            self.s.append(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)