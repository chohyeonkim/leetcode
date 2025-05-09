class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()

        res = []

        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums)):

                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                l = j + 1
                r = len(nums) - 1

                while l < r:
                    compare_sum = nums[i] + nums[j] + nums[l] + nums[r]

                    if target > compare_sum:
                        l += 1

                    elif target < compare_sum:
                        r -= 1

                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])

                        l += 1
                        r -= 1

                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1

        return res
