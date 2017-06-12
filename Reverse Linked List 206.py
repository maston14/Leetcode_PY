# Origin
# each time insert one at the head
import ListNode
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        dummy = ListNode(0)
        dummy.next = head

        p = head.next

        while p:
            head.next = p.next
            p.next = dummy.next
            dummy.next = p
            p = head.next

        return dummy.next

# don't insert, change the pointer from the head
class Solution2(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        cur = head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev

# Recursive
# 把tail从最底层，一层层return上来，每一层return的值都是一样的
class Solution3(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.reverse(None, head)

    def reverse(self, prev, cur):
        if not cur:
            return prev
        tmp = cur.next
        cur.next = prev
        return self.reverse(cur, tmp)