class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # tokens = ["1","2","+","3","*","4","-"]
        #                                    !
        # [5]    9 - 4 (first) - second

        op_set = set()
        op_set.add("+")
        op_set.add("*")
        op_set.add("-")
        op_set.add("/")

        stack = []

        for t in tokens:

            if t not in op_set:
                stack.append(t)
                continue

            second = int(stack.pop())
            first = int(stack.pop())

            if t == "+":
                stack.append(first + second)

            elif t == "-":
                stack.append(first - second)

            elif t == "*":
                stack.append(first * second)

            elif t == "/":
                stack.append(first / second)

        return int(stack[-1])
