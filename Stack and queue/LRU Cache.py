class LRUCache:

    def __init__(self, capacity: int):
        self.d = OrderedDict()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key in self.d:
            self.d.move_to_end(key)
            return self.d[key]
        return -1

    def put(self, key: int, value: int) -> None:

        if key in self.d or len(self.d) < self.cap:
            self.d[key] = value
            self.d.move_to_end(key)
        else:
            self.d.popitem(0)
            self.d[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
