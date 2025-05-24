class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        #  [(30 0),(38 1),(30 2), (36 3), (35 4), (40 5), (28 6)]
        #  [(40,5) (36 3) (30 2)] ()
        #  [1,4,1,2,1,0,0]

        res = []
        stack = []

        for i in range(len(temperatures) - 1, -1, -1):

            while stack and stack[-1][0] <= temperatures[i]:
                stack.pop()

            if stack:
                val, index = stack[-1]

                res.append(index - i)
            else:
                res.append(0)

            stack.append((temperatures[i], i))

        res.reverse()

        return res
