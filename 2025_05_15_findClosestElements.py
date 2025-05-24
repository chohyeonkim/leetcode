class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # sorted
        # return k closest int to x in the array
        # res should be sorted in asc order
        # can be nagative number.
        # duplicate?

        # 1) -
        # 2)
        #
        # brute force // -> use binary search to find the index
        #  [-5 -3, -2, 2, 4, 5, 8 10 12]
        #                 l    !r
        #                      6
        # [5 4 8]
        # find index when arr[i] > 6
        #

        left = 0
        right = len(arr) - 1

        while left <= right:

            mid = (left + right) // 2

            if arr[mid] < x:
                left = mid + 1

            elif arr[mid] > x:
                right = mid - 1

            else:
                left = mid
                break

        l = left - 1
        r = left

        res = []

        print(f"l {left - 1}")
        print(f"r {left}")

        while l >= 0 and r < len(arr) and len(res) < k:

            abs_left = abs(arr[l] - x)
            abs_right = abs(arr[r] - x)

            if abs_left <= abs_right:
                res.append(arr[l])
                l -= 1
            else:
                res.append(arr[r])
                r += 1

        if len(res) < k and l < 0:
            res.extend(arr[r : r + k - len(res)])

        elif len(res) < k and r >= len(arr):
            res.extend(arr[l - (k - len(res)) + 1 : l + 1])

        res.sort()

        return res
