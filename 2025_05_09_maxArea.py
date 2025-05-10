class Solution:
    def maxArea(self, heights: List[int]) -> int:

        #  [1,7,2,5,4,7,3,6]
        #     ! !
        #  7
        # 36
        # 15
        # 28
        # 12
        # 10
        # 2

        l = 0
        r = len(heights) - 1
        length = None
        max_output = 0

        while l < r:

            length = r - l

            h = min(heights[l], heights[r])

            output = h * length

            max_output = max(max_output, output)

            if heights[l] < heights[r]:
                l += 1

            elif heights[l] > heights[r]:
                r -= 1

            else:

                if l + 1 < r - 1:

                    if heights[l + 1] < heights[r - 1]:
                        r -= 1
                    else:
                        l += 1
                else:

                    r -= 1

        return max_output
