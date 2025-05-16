class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        # [5,1,6]
        #  ! ! !
        # [5] [1] [6]

        res = 0

        def backtrack(i, total) -> int:

            if i == len(nums):
                return total

            # include index i
            include_i = backtrack(i + 1, total ^ nums[i])

            exclude_i = backtrack(i + 1, total)

            return include_i + exclude_i

        return backtrack(0, 0)
