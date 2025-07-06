# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# l1 = [1,2,3]
# 1 + 20 + 300 = 3 2 1
# l2 = [4,5,6]
# 4 + 50 + 600 = 6 5 4
# 321 + 654 = 975
# 9 7 5 % 10 = 5
# 9 7 5 // 10 = 97
# 9 7 % 10 = 7
# 9 7 // 10 = 9
# 9 % 10 = 9
# 9 // 10 = 0
# if == 0 stop
# 5 7 9


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        num1 = 0
        num2 = 0

        digit = 1
        while l1:
            n = l1.val * digit
            num1 += n

            digit = digit * 10
            l1 = l1.next

        digit = 1
        while l2:
            n = l2.val * digit
            num2 += n

            digit = digit * 10
            l2 = l2.next

        # print(num1)
        # print(num2)
        # print(num1 + num2)

        sum_num = num1 + num2

        dummy = ListNode(0)
        start = dummy

        if sum_num == 0:
            return dummy

        while sum_num != 0:

            val = sum_num % 10
            start.next = ListNode(val)

            sum_num = sum_num // 10
            start = start.next

        return dummy.next
