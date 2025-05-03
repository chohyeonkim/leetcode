class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        c1, c2, = 0, 0

        res = []

        while c1 < len(word1) and c2 < len(word2):

            res.append(word1[c1])
            res.append(word2[c2])

            c1 += 1
            c2 += 1

        print(res)

        if c1 < len(word1):
            res.extend(word1[c1:])
        else:
            res.extend(word2[c2:])

        return "".join(res)
