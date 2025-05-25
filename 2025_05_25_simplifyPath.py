class Solution:
    def simplifyPath(self, path: str) -> str:
        # "/neetcode/practice//...///../courses"
        # skip "."
        # ".." pop
        # remove all // /// /
        #
        #  "needcode" "practice"  "courses"
        # ..

        path_no_split = path.split("/")

        res = []

        for p in path_no_split:

            if p == "." or p == "":
                continue

            if p == "..":

                if res:
                    res.pop()
                continue

            res.append(p)

        print(res)

        return "/" + "/".join(res)
