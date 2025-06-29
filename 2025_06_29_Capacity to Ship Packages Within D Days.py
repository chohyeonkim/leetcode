class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # min capacity = 5
        #
        # [1,5,4,4,2,3]
        #  1/5/4/4/23 -> 5 ships

        # l = lower bound
        # r = upper bound

        left = max(weights)  # lower bound
        right = sum(weights) # upper bound

        res = sum(weights) 


        while (left <= right):

            mid = (left + right) // 2

            capacity = mid
            ship = 1

            for w in weights:

                if capacity - w < 0:
                    ship += 1
                    capacity = mid
                
                capacity -= w

            if ship > days:
                # increase res
                left = mid + 1

            elif ship <= days:
                # decrease res
                res = min(res, mid)
                right = mid - 1

        return res

