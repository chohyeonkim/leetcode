class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # [1   2  8  48 ]
        # [48  48  24  6]
        #  48  24  12  8

        forward = []
        reverse = []

        for i in range (len(nums)):

            if i == 0:
                forward.append(nums[i])
                reverse.append(nums[-1])

            else:
                forward.append(forward[i-1] * nums[i])
                j = i + 1
                reverse.append(reverse[i-1] * nums[-j])
        reverse = reverse[::-1]

        res = []

        for i in range(len(nums)):

            front = i - 1
            back = i + 1

            val = None

            if front >= 0 and back < len(nums):
                val = forward[front] * reverse[back]
            elif front >= 0:
                val = forward[front]
            elif back < len(nums):
                val = reverse[back]

            res.append(val)

        return res