# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast,prev = head,head,None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        if not prev:
            return
        prev.next = None

        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        first = head
        second = prev
        curr = ListNode()
        while first:
            curr.next = first
            first = first.next
            curr = curr.next

            curr.next = second
            second = second.next
            curr = curr.next