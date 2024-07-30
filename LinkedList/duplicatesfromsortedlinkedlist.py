# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        cn=head
        while cn:
            while cn.next and cn.val==cn.next.val:
                cn.next=cn.next.next
            cn=cn.next
        return head 
