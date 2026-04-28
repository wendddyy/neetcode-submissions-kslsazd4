import bisect
class TimeMap:

    def __init__(self):
        self.times = defaultdict(list)
        self.vals = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.times[key].append(timestamp)
        self.vals[key].append(value)


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.times:
            return ""
        
        tlist = self.times[key]
        index = bisect.bisect_right(tlist, timestamp) - 1
        if index < 0:
            return ""
        return self.vals[key][index]