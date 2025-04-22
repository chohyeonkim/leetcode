# https://leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        left, right = 0, len(nums) - 1

        while left <= right:

            if nums[left] == val:
                while left < right and nums[right] == val:
                    right -= 1 # val가 아닐때 stop

                nums[left] = nums[right]

                right -= 1

            else:
                left += 1


        return left
