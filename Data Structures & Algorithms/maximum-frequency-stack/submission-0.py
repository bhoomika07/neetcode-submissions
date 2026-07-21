class FreqStack:

    def __init__(self):
        self.stack = []
        self.hash_map = {}
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val in self.hash_map:
            self.hash_map[val]+=1
        else:
            self.hash_map[val] = 1
        
    def pop(self) -> int:
        max_freq = max(self.hash_map.values())
        for i in range(len(self.stack) - 1, -1, -1):
            val = self.stack[i]
            if self.hash_map.get(val, 0) == max_freq:
                self.stack.pop(i)
                self.hash_map[val] -= 1
                if self.hash_map[val] == 0:
                    del self.hash_map[val]
                return val
            



        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()