class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l, r = 0, len(numbers) - 1

        while l < r:

            curr = numbers[l] + numbers[r]

            if curr < target:
                l = l + 1

            elif curr > target:
                r = r - 1

            else:
                return [l + 1, r + 1]
