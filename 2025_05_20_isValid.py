class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        # odd length = false
        stack = []

        for c in s:
            if c not in parentheses:
                stack.append(c)
                continue

            top = None

            if stack:
                top = stack.pop()

            if top != parentheses[c]:
                return False

        return False if stack else True
