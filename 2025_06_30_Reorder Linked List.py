# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# [0, 1, 2, 3, 4, 5, 6  7]
#           s
#                    f  (fast.next = none stop)
#  0  1  2  3
#  1) find the middle point (slow/fast)  slow (middle)
#  [0 1 2 3] [4 5 6]
#   h
#  [6 5 4] reversed the second part
#
#  2) merge the 2 linked list
#


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # find the middle point
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        second_start = slow.next
        slow.next = None  # break the part

        # reversed the second
        pre = None
        cur = second_start

        while cur:
            nt = cur.next
            cur.next = pre

            pre = cur
            cur = nt

        # [0 1 2 3]
        # [6 5 4]
        # merge the 2 linked list
        list1 = head
        list2 = pre

        while list1 and list2:

            nt_list1 = list1.next
            list1.next = list2

            nt_list2 = list2.next
            list2.next = nt_list1

            list1 = nt_list1
            list2 = nt_list2
