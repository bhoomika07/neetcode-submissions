class MyHashMap:

    def __init__(self):
        print("Initialising hash map")
        self.hash_map = {}
        

    def put(self, key: int, value: int) -> None:
        print(f"Adding {key} in hash map")
        if key not in self.hash_map:
            self.hash_map[key] = value
        else:
            self.hash_map[key] = value

        

    def get(self, key: int) -> int:
        print(f"Getting {key} in hash map")
        if key in self.hash_map:
            return self.hash_map[key]
        else:
            return -1
        

    def remove(self, key: int) -> None:
        print(f"Removing {key} in hash map")
        if key in self.hash_map:
            self.hash_map.pop(key)

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)