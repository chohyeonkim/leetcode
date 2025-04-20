# https://leetcode.com/problems/simplify-path/description/?envType=problem-list-v2&envId=eh31chej

class Solution:
    def simplifyPath(self, path: str) -> str:
        # .
        # ..
        # any # of slash //,  /// -> /
        # else valid directory or file name
        # 1) start with '/'
        # 2) separate by one slash '/'
        # 3) not end with '/'
        # 4) No . or .. in the path

        print(path.split("/"))

        split_path = path.split("/")

        stack_res = []
        for s in split_path:

            if s == "." or s == "":  # single period or empty string
                continue
            if s == "..":
                if stack_res:
                    stack_res.pop()
            else:
                stack_res.append(s)

        return "/" + ("/").join(stack_res)
