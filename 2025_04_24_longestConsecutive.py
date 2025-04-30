class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums_dict = set(nums)
        longest_sequence = 0

        for num in nums:

            # start point
            if num - 1 not in nums_dict:

                start = num
                sequence = 0

                while start in nums_dict:

                    sequence += 1
                    start += 1

                longest_sequence = max(longest_sequence, sequence)
            else:
                continue

        return longest_sequence
