class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # k = 2 (at most k replacement)
        # XYYX
        # !  !
        # X : 2 , Y: 2
        # AAABABB
        #       !
        # A:1, B = 2
        # count = 5
        # A랑 B중에 뭐가 더 most frequent인지는 어떻게 알지..? -> max
        # ABABABACACAC

        l = 0

        frequency_map = collections.defaultdict(int)
        max_count = 0

        for r in range(len(s)):

            frequency_map[s[r]] += 1

            max_val = max(frequency_map.values())

            while r - l + 1 - max_val > k:

                frequency_map[s[l]] -= 1
                l += 1

            max_count = max(max_count, r - l + 1)

        return max_count
