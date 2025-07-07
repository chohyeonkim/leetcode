class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # sorting (easiest way)
        # start from [0] (n + 1)  [1, n]
        #         i
        # [ 1 ,3, 4 ,2,2]
        #  -1 -3 -4 -2
        # iterate -> index + 1 mark negative

        for i in range(len(nums)):
            number = abs(nums[i])
            index = number - 1

            if nums[index] < 0:
                return number
            else:
                nums[index] = -nums[index]

        return -1
