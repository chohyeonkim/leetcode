class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(arr1, arr2):
            res = []
            i = 0
            j = 0
            while i < len(arr1) and j < len(arr2):

                if arr1[i] >= arr2[j]:
                    res.append(arr2[j])
                    j += 1

                else:
                    res.append(arr1[i])
                    i += 1

            if i < len(arr1):
                res = res + arr1[i:]

            elif j < len(arr2):
                res = res + arr2[j:]

            return res

        def mergeSort(arr):

            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2

            left_subarr = mergeSort(arr[:mid])
            right_subarr = mergeSort(arr[mid:])

            return merge(left_subarr, right_subarr)

        return mergeSort(nums)
