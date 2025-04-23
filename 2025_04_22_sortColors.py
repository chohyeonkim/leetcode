class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # count_dict = {0: 0, 1: 0, 2:0}
        # for num in nums:
        #     count_dict[num] += 1

        # index = 0
        # key = 0
        # while key < 3:
        #     if count_dict[key] != 0:
        #         nums[index] = key
        #         count_dict[key] -= 1
        #         index += 1
        #     else:
        #         key += 1

        left, right = 0, len(nums) - 1
        i = 0

        while left < right and i <= right:

            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                i += 1
                left += 1

            elif nums[i] == 1:
                i += 1

            else:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
