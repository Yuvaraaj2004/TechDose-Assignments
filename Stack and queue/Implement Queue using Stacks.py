class MyQueue:

    def __init__(self):
        self.stack = []
        self.queue = []

    def push(self, x: int) -> None:
        print(self.queue, self.stack)
        self.stack.append(x)

    def pop(self) -> int:
        print(self.queue, self.stack)
        self.queue = [self.stack.pop()
                      for i in range(len(self.stack))]+self.queue
        return self.queue.pop()

    def peek(self) -> int:
        print(self.queue, self.stack)
        self.queue = [self.stack.pop()
                      for i in range(len(self.stack))]+self.queue
        return self.queue[-1]

    def empty(self) -> bool:
        print(self.queue, self.stack)
        self.queue = [self.stack.pop()
                      for i in range(len(self.stack))]+self.queue
        return not (self.queue)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
