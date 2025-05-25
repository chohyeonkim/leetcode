class MyQueue:
    # 1 2 3

    # F [6 7 8 9 10] push
    # B []

    def __init__(self):
        self.push_stack = []
        self.pop_stack = []

    def push(self, x: int) -> None:
        self.push_stack.append(x)

    def pop(self) -> int:

        if self.pop_stack:
            return self.pop_stack.pop()

        while self.push_stack:
            ele = self.push_stack.pop()
            self.pop_stack.append(ele)

        return self.pop_stack.pop()

    def peek(self) -> int:

        if self.pop_stack:
            return self.pop_stack[-1]

        while self.push_stack:
            ele = self.push_stack.pop()
            self.pop_stack.append(ele)

        return self.pop_stack[-1]

    def empty(self) -> bool:

        return True if not self.pop_stack and not self.push_stack else False
