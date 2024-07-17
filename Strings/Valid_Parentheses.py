class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        
        d={'(':')','{':'}','[':']'}
        for c in s:
            if c in d:
                stack.append(c)
            elif len(stack)>0:
                if c in d.values():
                    top=stack.pop()
                    if c!=d[top]:
                        return False
            else:
                return False
               
                    
        if stack!=[]:
            return False
        else:
            return True
                
            
        
