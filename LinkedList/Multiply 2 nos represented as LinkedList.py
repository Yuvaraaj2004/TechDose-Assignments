# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def rec(node=head):
            if not node:
                return 0
            else:
                c = node.val*2//10
                node.val = (node.val*2 if node.val*2 <
                            10 else node.val*2 % 10)+rec(node.next)
                return c
        v = rec()
        if v:
            l = ListNode(v)
            l.next = head
            head = l
        return head
