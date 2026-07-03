class MyHashMap:

    def __init__(self):
        self.size = 2069
        self.hash_map = [-1]*2069
    
    def _hash(self, key: int):
        return key%self.size
        

    def put(self, key: int, value: int) -> None:
        idx = self._hash(key)
        self.hash_map[idx] = value
 

    def get(self, key: int) -> int:
        idx = self._hash(key)
        return self.hash_map[idx]
        

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        self.hash_map[idx] = -1

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)