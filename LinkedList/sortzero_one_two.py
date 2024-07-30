'''
Given a linked list of N nodes where nodes can contain values 0s, 1s, and 2s only. The task is to segregate 0s, 1s, and 2s linked list such that all zeros segregate to head side, 2s at the end of the linked list, and 1s in the mid of 0s and 2s.
'''
class Node:
    
	def __init__(self, data):
	    # data -> value stored in node
		self.data = data
		self.next = None
	

class Solution:
    #Function to sort a linked list of 0s, 1s and 2s.
    def segregate(self, head):
        #code here
        cn=head
        ll=[]
        if cn is None:
            return None
        while cn:
            ll.append(cn.data)
            cn=cn.next
        ll=sorted(ll)
        cn=head
        i=0
        while cn:
            cn.data=ll[i]
            cn=cn.next
            i+=1
       # cn.next=None
        return head
                
            
