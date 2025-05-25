class Solution:
    def decodeString(self, s: str) -> str:
        # "2[a3[b]]c"
        #  stack = 2[abbb]
        #   abbbabbbc

        stack = []

        for c in s:

            if c != "]":
                stack.append(c)
                continue

            repeat_word = ""
            while stack and stack[-1] != "[":
                repeat_word = stack.pop() + repeat_word

            stack.pop()  # remove "["

            k = ""
            while stack and stack[-1].isdigit():
                k = stack.pop() + k

            stack.append(int(k) * repeat_word)

        return "".join(stack)
