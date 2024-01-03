# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def remove(root):
            while (root != None):
                temp = root.next
                while (temp != None and temp.val == root.val):
                    temp = temp.next
                root.next = temp
                root = root.next

        remove(head)
        return head
