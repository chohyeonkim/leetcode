class Solution:
    def isPalindrome(self, s: str) -> bool:

        # str.isalnum()
        # str.lower

        new_string = []
        for c in s:
            if c.isalnum():
                lower_c = c.lower()
                new_string.append(lower_c)

        left, right = 0, len(new_string) - 1
        while left <= right:
            if new_string[left] != new_string[right]:
                return False

            left += 1
            right -= 1

        return True
