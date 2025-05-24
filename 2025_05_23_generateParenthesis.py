class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # generate all possible combination of parentheses
        # stop when len()  == 2 * n
        # when len("(") == open < close -> invalid

        # check if it's valid stack..?

        res = []

        def backtrack(combination: List[str], op, cl):

            # invalid
            if op < cl or (len(combination) == 2 * n and op != cl):
                print(f"op {op} cl {cl}")
                print(combination)
                return

            # valid but end
            if len(combination) == 2 * n:
                print(f"valid op {op} cl {cl}")
                print(combination)
                res.append("".join(combination))
                return

            # backtrack
            combination.append("(")
            backtrack(combination, op + 1, cl)
            combination.pop()

            combination.append(")")
            backtrack(combination, op, cl + 1)
            combination.pop()

        backtrack([], 0, 0)
        return res
