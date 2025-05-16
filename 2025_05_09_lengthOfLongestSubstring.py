class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # "zxyzxyz"
        #      s
        #        e
        # set = {z x y}

        duplicate_set = set()
        l, r = 0, 0
        max_length = 0

        while r < len(s):

            if s[r] not in duplicate_set:
                duplicate_set.add(s[r])
                length = r - l + 1
                max_length = max(max_length, length)

                r += 1

            else:  # when s[r] is in duplicate set
                while s[l] != s[r]:
                    duplicate_set.remove(s[l])
                    l += 1
                duplicate_set.remove(s[l])
                l += 1

        return max_length
