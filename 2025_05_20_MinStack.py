class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        # self.min_number = float('inf')
        # getMin
        # [5 6 3 5 1 4]
        # [5 5 3 3 1 1]

    def push(self, val: int) -> None:

        if not self.min_stack or self.min_stack[-1] > val:
            self.min_stack.append(val)

        else:
            self.min_stack.append(self.min_stack[-1])

        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
