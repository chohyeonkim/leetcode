# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Input: head = [1,2,3,4,5], left = 1, right = 3

# [1,2,  3, 4,5]
#  l<- <-r  n
#  1  4  3  2 5


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:

        # pre_left
        # left
        # right
        # right_next

        dummy = ListNode(0, head)
        pre_left, left_node = dummy, head

        count = 1
        while count != left:
            pre_left = left_node
            left_node = left_node.next
            count += 1

        prev = None
        cur = left_node
        for i in range(right - left + 1):
            nt = cur.next
            cur.next = prev
            prev = cur
            cur = nt

        # Important !

        pre_left.next.next = cur
        pre_left.next = prev

        return dummy.next
