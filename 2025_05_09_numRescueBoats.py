class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        # [1,3,2,3,2]
        # 1 2 2 3 3
        #   !!
        # limit = 3
        # when r = l ?

        people.sort()

        l, r = 0, len(people) - 1
        count = 0

        while l < r:

            people_sum = people[l] + people[r]

            if limit >= people_sum:
                l += 1
                r -= 1

            else:
                r -= 1

            count += 1

        if l == r:
            count += 1

        return count
