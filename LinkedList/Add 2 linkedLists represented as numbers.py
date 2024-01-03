# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, lis1: Optional[ListNode], lis2: Optional[ListNode]) -> Optional[ListNode]:
        def String(node):
            if node:
                if node.next:
                    return String(node.next)+str(node.val)
                else:
                    return str(node.val)
        root = ListNode()
        temp = root
        v = str(int(String(lis1))+int(String(lis2)))[::-1]
        leng = len(v)
        for i in range(leng):
            temp.val = int(v[i])
            if i+1 < leng:
                temp.next = ListNode()
                temp = temp.next
        return root
