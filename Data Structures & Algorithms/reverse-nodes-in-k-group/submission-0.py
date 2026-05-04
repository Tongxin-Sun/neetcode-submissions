# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        cur = head
        for i in range(k - 1):
            cur = cur.next
            if not cur:
                return head
        nextList = cur.next
        cur.next = None
        newHead = self.reverseList(head)
        cur = newHead
        while cur.next:
            cur = cur.next
        cur.next = self.reverseKGroup(nextList, k)
        return newHead
    
    def reverseList(self, head):
        if not head.next:
            return head
        res = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return res