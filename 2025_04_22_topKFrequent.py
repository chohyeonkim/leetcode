class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count_dict = {}

        for num in nums:

            if num not in count_dict:
                count_dict[num] = 1

            else:
                count_dict[num] += 1

        bucket = [[] for _ in range(len(nums))]

        for key, val in count_dict.items():
            bucket[val - 1].append(key)

        res = []

        j = len(nums) - 1

        while j >= 0 and len(res) < k:

            if len(bucket[j]) != 0:
                res = res + bucket[j]

            j -= 1

        return res[:k]
