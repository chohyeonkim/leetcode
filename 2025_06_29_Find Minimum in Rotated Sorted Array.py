class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 0 1 2 3 4 5
        # 3,4,5,6,1,2
        #       l m r
        #
        # check mid , mid + 1 ?
        # l = mid + 1
        # l > m # pivot btw from l to m
        # r = m - 1
        #

        l = 0
        r = len(nums) - 1

        res = nums[0]

        while l <= r:

            mid = (l + r) // 2

            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            res = min(res, nums[mid])

            if nums[l] <= nums[mid]:  #
                l = mid + 1
            else:
                r = mid - 1

        return res
