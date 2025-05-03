class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # [10,20,10,10,20,20 40]
        #        !
        # # [1 2 10]
        #      !

        nums1_pointer = m - 1
        nums2_pointer = len(nums2) - 1

        for insert_pointer in range(len(nums1) - 1, -1, -1):

            insert_val = None

            if nums1_pointer >= 0 and nums2_pointer >= 0:
                if nums1[nums1_pointer] > nums2[nums2_pointer]:
                    insert_val = nums1[nums1_pointer]
                    nums1_pointer -= 1

                else:
                    insert_val = nums2[nums2_pointer]
                    nums2_pointer -= 1

            elif nums1_pointer >= 0:
                insert_val = nums1[nums1_pointer]
                nums1_pointer -= 1

            elif nums2_pointer >= 0:
                insert_val = nums2[nums2_pointer]
                nums2_pointer -= 1

            nums1[insert_pointer] = insert_val
