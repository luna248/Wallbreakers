class LFUCache:

    def __init__(self, capacity: int):
        self.freqMap = dict()
        self.lruMap = defaultdict(OrderedDict)
        self.capacity = capacity
        self.lruParser = 1

    def get(self, key: int) -> int:
        if key not in self.freqMap or self.capacity == 0:
            return -1

        currFreq = self.freqMap[key]
        val = self.lruMap[currFreq][key]
        del self.lruMap[currFreq][key]

        self.lruMap[currFreq+1][key] = val
        self.freqMap[key] += 1
        return val

    def put(self, key: int, value: int) -> None:
        if self.capacity==0:
            return

        if key not in self.freqMap and len(self.freqMap)==self.capacity:
            while len(self.lruMap[self.lruParser]) == 0:
                self.lruParser+=1
            keyToBeDeleted = self.lruMap[self.lruParser].popitem(last=False)[0]
            del self.freqMap[keyToBeDeleted]

        if key in self.freqMap:
            currFreq = self.freqMap[key]

            #Update to new frequency in frequency map
            self.freqMap[key] += 1

            #Update to new frequency in lruMap
            del self.lruMap[currFreq][key]
            self.lruMap[currFreq+1][key] = value
        else:
            self.freqMap[key] = 1
            self.lruMap[1][key] = value
            self.lruParser = 1



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
