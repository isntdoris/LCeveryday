class RandomizedSet:

    def __init__(self):
        self.numMap = {}
        self.numList = []

    def insert(self, val: int) -> bool:
        res = val not in self.numMap
        if res:
            self.numMap[val] = len(self.numList)
            self.numList.append(val)
        return res

    def remove(self, val: int) -> bool:
        res = val in self.numMap
        if res:
            # 以下執行順序要注意，否則容易runtime error
            idx = self.numMap[val]
            self.numList[idx] = self.numList[-1]
            self.numMap[self.numList[-1]] = idx
            self.numList.pop()
            del self.numMap[val]
        return res

    def getRandom(self) -> int:
        return random.choice(self.numList)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()