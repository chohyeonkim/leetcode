class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        # remove all negative sign
        for i in range(len(nums)):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1

        for i in range(len(nums)):
            compare = abs(nums[i])
            if compare > 0 and compare <= len(nums):
                val = nums[compare - 1]
                if val >  0 and val != 0:
                    nums[compare - 1] = -val
                elif val < 0:
                    continue
                else:
                    nums[compare - 1] = -(len(nums) + 2)

        for i in range(len(nums)):

            if nums[i] > 0:
                return i + 1

        return len(nums) + 1