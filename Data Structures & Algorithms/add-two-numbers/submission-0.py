# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        remainder = 0
        dummy = cur = ListNode()
        while l1 and l2:
            newNode = ListNode((l1.val + l2.val + remainder) % 10)
            remainder = (l1.val + l2.val + remainder) // 10
            cur.next = newNode
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            newNode = ListNode((l1.val + remainder) % 10)
            remainder = (l1.val + remainder) // 10
            cur.next = newNode
            cur = cur.next
            l1 = l1.next
        while l2:
            newNode = ListNode((l2.val + remainder) % 10)
            remainder = (l2.val + remainder) // 10
            cur.next = newNode
            cur = cur.next
            l2 = l2.next
        if remainder != 0:
            newNode = ListNode(remainder)
            cur.next = newNode
        return dummy.next