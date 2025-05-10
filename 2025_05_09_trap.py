class Solution:
    def trap(self, height: List[int]) -> int:

        # min(height[l], height[r]) - height[i]

        #   [0,2,0,3,1,0,1,3,2,1]
        # L  0 0 2 2 3 3 3 3 3 3
        # R  3 3 3 3 3 3 3 2 1 0
        #    0 0 2 2 3 3 3 2 1 1
        #    0 0 2 0 2 3 2 0 0 0 = 9

        # maxleft, maxright pointer 가지고도 space complexity O(1)로 해결 가능

        presum = [0] * len(height)
        suffix = [0] * len(height)

        for i in range(len(height) - 1):
            presum[i + 1] = max(presum[i], height[i])

            reverse_index = len(height) - 1 - i

            suffix[reverse_index - 1] = max(
                suffix[reverse_index], height[reverse_index]
            )

        print(presum)
        print(suffix)

        output = 0

        for i in range(len(height)):

            min_height = min(presum[i], suffix[i])

            water = min_height - height[i]

            if water > 0:
                output += water

        return output
