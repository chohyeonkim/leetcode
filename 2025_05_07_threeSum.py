class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # brute force (3 loops)
        #  sort [-1,0,1,2,-1,-4] -> [ -4 -1 -1 0 1 2 ]
        # nums[i] + nums[j] == - nums[k] (target)
        # -nums[i] = nums[j] + nums[k]

        # sorting needed? (other wise we dont we which pointer to move)
        # [ -4 -1 -1 0 1 2 ]
        #   4 =        ! ! = 3
        #   1 = -1 2 만약에 같으면 바로 break가 아니라 하나 옮겨서 다시?
        #   1 =  0 1

        # sort
        nums.sort()
        print(nums)

        res = []

        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]

            l = i + 1
            r = len(nums) - 1

            while l < r:

                compare_sum = nums[l] + nums[r]

                print(compare_sum)

                if target == compare_sum:
                    res.append([nums[i], nums[l], nums[r]])

                    l += 1
                    r -= 1

                    while nums[r] == nums[r + 1] and l < r:
                        r -= 1

                elif target > compare_sum:

                    l += 1

                else:
                    r -= 1

        return res
