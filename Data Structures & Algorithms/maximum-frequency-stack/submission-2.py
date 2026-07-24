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
        max_frequency = max(self.hash_map.values())

        # Find the most recent element having max frequency
        for i in range(len(self.stack) - 1, -1, -1):
            if self.hash_map[self.stack[i]] == max_frequency:
                max_freq_key = self.stack.pop(i)
                break

        self.hash_map[max_freq_key] -= 1
        if self.hash_map[max_freq_key] == 0:
            del self.hash_map[max_freq_key]

        return max_freq_key


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()