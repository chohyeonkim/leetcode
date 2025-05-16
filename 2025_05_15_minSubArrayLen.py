class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # target
        # min length of subarry >= target
        # contiguous ( non empty)
        # [2,1,5,1,5,3]
        #            !
        #        !
        #  3

        l = 0
        min_length = float("inf")
        acc_sum = 0

        for r in range(len(nums)):

            acc_sum += nums[r]

            if acc_sum < target:
                continue

            while acc_sum >= target:
                min_length = min(min_length, r - l + 1)

                acc_sum -= nums[l]
                l += 1

        if min_length > len(nums):
            return 0

        return min_length
