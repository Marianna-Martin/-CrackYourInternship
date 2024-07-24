class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        s=""
        t=columnNumber
        while(columnNumber>0):
            d=(columnNumber-1)%26
            s=s+chr(65+d)
            columnNumber=(columnNumber-1)//26
            
        
           

                    
                   
                   
            
        
                
        return s[::-1]
                

