class Solution:
    def validPalindrome(self, s: str) -> bool:

        #'aabda'
        #   !
        # how you know move left or right?
        # 'bd' remove left
        # 'ab' remove right
        # any of them panlindrom is true

        def helper(sub_s: str) -> bool:
            l, r = 0, len(sub_s) - 1

            while l <= r:

                if sub_s[l] != sub_s[r]:
                    return False

                l += 1
                r -= 1

            return True

        left, right = 0, len(s) - 1

        while left <= right:

            if s[left] != s[right]:

                return helper(s[left + 1 : right + 1]) or helper(s[left:right])

            left += 1
            right -= 1

        return True
