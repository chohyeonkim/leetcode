# https://leetcode.com/problems/longest-common-prefix/
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        compare = strs[0]

        min_prefix = len(compare)

        for str in strs:

            c, j = 0, 0  # pointer

            prefix = []

            while c < len(compare) and j < len(str):

                if compare[c] == str[j]:
                    prefix.append(compare[c])
                    c += 1
                    j += 1

                else:
                    break

            compare_prefix = "".join(prefix)

            min_prefix = min(min_prefix, len(compare_prefix))

        return compare[:min_prefix]
