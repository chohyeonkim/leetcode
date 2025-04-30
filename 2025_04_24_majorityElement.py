class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        m1, m2, count1, count2 = 0, 0, 0, 0

        for num in nums:

            if num == m1:
                count1 += 1
            elif num == m2:
                count2 += 1
            elif count1 == 0:
                m1 = num
                count1 += 1
            elif count2 == 0:
                m2 = num
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1

        print(m1, m2)
 
        count1, count2 = 0, 0

        for num in nums:
            if num == m1:
                count1 += 1
            elif num == m2:
                count2 += 1

        print(count1, count2)

        res = []

        if count1 > len(nums) // 3:
            res.append(m1)

        if count2 > len(nums) // 3:
            res.append(m2)

        return res

        


            