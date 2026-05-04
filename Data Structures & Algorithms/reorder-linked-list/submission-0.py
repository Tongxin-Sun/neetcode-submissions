# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverseList(head):
            slow = head
            fast = head.next
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            t = slow.next
            slow.next = None
            slow = t
            prev = None
            while slow:
                nxt = slow.next
                slow.next = prev
                prev = slow
                slow = nxt
            return prev
        p1, p2 = head, reverseList(head)
        while p2:
            t = p1.next
            p1.next = p2
            p1 = t
            
            t = p2.next
            p2.next = p1
            p2 = t
        print(head.val)