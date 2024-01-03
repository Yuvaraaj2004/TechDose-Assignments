# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        temp = head
        while (temp != None):
            nxt = temp.next
            temp.next = pre
            pre = temp

            temp = nxt
        return pre
