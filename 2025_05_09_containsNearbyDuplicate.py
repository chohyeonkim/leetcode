class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        distinct_set = set()
        s = 0
        e = 0
        while e < len(nums):
            # window size is smaller than k
            if e - s <= k:
                if nums[e] not in distinct_set:
                    distinct_set.add(nums[e])

                    # increase the window size
                    e += 1
                else:
                    print(f"e:{e}, s:{s}")
                    print(distinct_set)
                    return True

            else:
                distinct_set.remove(nums[s])
                s += 1

        print(distinct_set)

        return False
