class MyStack:

    def __init__(self):
        self.queue1 = []

    def push(self, x: int) -> None:
        # Instead of appending and reversing the whole thing,
        # put the new element at the front of the list.
        self.queue1 = [x] + self.queue1

    def pop(self) -> int:
        return self.queue1.pop(0)

    def top(self) -> int:
        return self.queue1[0]

    def empty(self) -> bool:
        return len(self.queue1) == 0