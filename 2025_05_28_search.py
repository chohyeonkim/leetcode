class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #  0 1 2 3 4 5 6
        # [4,5,6,7,0,1,2]
        #  l   m    m    r
        #      m    m
        # 1 2 3 4 5 6
        # l   m    r
        #  nums[l] < nums[m]  -- -> pivot point is left side
        #    nums[l] < target && target < nums[mid]
        #    -> r = mid - 1
        #    -> else l = mid + 1
        #
        #  nums[l] > nums[m]  --> pivot point is right side
        #   nums[m]< target  && target < nums[r]
        #   -> l = mid + 1
        #   -> r = mid -1
        #

        l = 0
        r = len(nums) - 1

        while l <= r:

            m = (l + r) // 2

            if target == nums[m]:
                return m

            if nums[l] <= nums[m]:
                if nums[l] <= target and target <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1

            else:
                if nums[m] <= target and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1
