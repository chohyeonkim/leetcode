class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # [1,2,3,4,5,6,7,8]
        #   8 7 6 5 4 3 2 1
        #   6 7 8 / 1 2 3 4 5
        #  [6,7,8,1,2,3,4,5]

        k = k % len(nums)

        nums.reverse()

        print(nums)

        l = 0
        r = k - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        l = k
        r = len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
