class MyQueue:
    def __init__(self):
        self.firstStack = []
        self.secondStack = []

    def push(self, x: int) -> None:
        self.firstStack.append(x)
        self.secondStack.append(self.firstStack.pop())

    def pop(self) -> int:
        return self.secondStack.pop(0)

    def peek(self) -> int:
        return self.secondStack[0]

    def empty(self) -> bool:
        return len(self.secondStack) == 0