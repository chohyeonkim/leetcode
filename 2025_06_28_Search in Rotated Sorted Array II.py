class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # since becuase of the duplicate
        # [1 0 1 1 1 1]  when l == mid does not matter where the mid point is
        #  l   m   m ?  <- but this right side
        # 3 possible cases
        # 1) l < mid
        # 2) mid < l
        # 3) mid == l
        l = 0
        r = len(nums) - 1

        while l <= r:

            mid = (l + r) // 2

            if nums[l] == target or nums[r] == target or nums[mid] == target:
                return True

            if nums[l] < nums[mid]:  # left side

                if nums[l] < target < nums[mid]:
                    r = mid - 1

                else:
                    l = mid + 1

            elif nums[l] > nums[mid]:  # right side

                if nums[mid] < target < nums[r]:
                    l = mid + 1

                else:
                    r = mid - 1

            else:  # when nums[l] == nums[mid]
                l += 1

        return False
