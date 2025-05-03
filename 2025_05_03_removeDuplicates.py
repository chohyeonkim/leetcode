class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 0,1,2,3,4,3,3,3,4,5
        #           l
        #                   r

        # increasing order
        # so when r reach a unique number it means it passes all previous number before

        n = len(nums) - 1

        l, r = 0, 0

        while r <= n:
            nums[l] = nums[r]
            while r <= n and nums[r] == nums[l]:
                r += 1
            l += 1

        return l
