class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head and head.val == val:
            head = head.next

        cn = head
        while cn and cn.next:
            if cn.next.val == val:
                cn.next = cn.next.next
            else:
                cn = cn.next

        return head
