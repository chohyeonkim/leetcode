class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []

        def backtrack(i, path):

            if i == len(nums):
                subsets.append(path[:])
                return

            # include nums[i]
            path.append(nums[i])
            backtrack(i + 1, path)

            # exclude nums[i]
            path.pop()
            backtrack(i + 1, path)

        backtrack(0, [])
        return subsets
