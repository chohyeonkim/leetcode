class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # permutation?
        # if s2 < s1 then false
        # 1..  "a", "b" X
        #
        # lecabee
        #  ! !
        # every len(s1).. compare the dictionary?
        # {l:1 e:1 c:1}
        # abc -> {a:1, b:1, c:1}

        s1_map = collections.Counter(s1)
        s2_map = collections.Counter(s2[: len(s1) - 1])

        res = False
        left = 0

        if len(s1) > len(s2):
            return False

        for right in range(len(s1) - 1, len(s2)):

            s2_map[s2[right]] = s2_map.get(s2[right], 0) + 1

            for key, value in s1_map.items():
                if s1_map[key] != s2_map[key]:
                    break

            else:
                res = True

            if res:
                break

            s2_map[s2[left]] -= 1
            left += 1

        return res
