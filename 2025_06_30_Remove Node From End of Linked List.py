# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # dummy -> head 구조로 만들면, head 제거도 slow.next = slow.next.next로 통일됨
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        for i in range(n + 1):
            if fast:
                fast = fast.next
                
        while fast:
            slow = slow.next
            fast = fast.next

        nt = slow.next.next
        slow.next = nt

        return dummy.next
