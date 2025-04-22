class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        count_map = {}

        for num in nums:

            if num not in count_map:
                count_map[num] = 1

            else:
                count_map[num] += 1

            if count_map[num] * 2 > len(nums):
                return num

        
