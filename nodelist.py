# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur, prev = head, None
        while cur:
            cur.next, cur, prev = prev, cur.next, cur
        cur = prev
        while cur:
            print(f'{cur.val}->', end='')
            cur = cur.next
        print('NULL')


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next, b.next, c.next, d.next, e.next = b, c, d, e, None
so = Solution()
so.reverseList(a)


