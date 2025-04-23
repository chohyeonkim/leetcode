class Solution:

    def encode(self, strs: List[str]) -> str:

        res = []

        for s in strs:
            str_length = len(s)

            res.append(str(str_length))
            res.append("#")
            res.append(s)

        print(res)

        return "".join(res)

    def decode(self, s: str) -> List[str]:

        i = 0
        res = []

        while i < len(s):

            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            print("length", length)

            i = j + length + 1

            word_list = []
            for start in range(length):

                word_list.append(s[j + start + 1])

            new_word = "".join(word_list)

            res.append(new_word)

        return res
