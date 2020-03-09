class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

a1 = ListNode(1)
a2 = ListNode(1)
b1 = ListNode(2)
b2 = ListNode(2)
c1 = ListNode(2)
c2 = ListNode(2)
d1 = ListNode(3)
d2 = ListNode(3)
a1.next = b1
a2.next = b2
b1.next = c1
b2.next = c2
c1.next = d1
c2.next = d2


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):

