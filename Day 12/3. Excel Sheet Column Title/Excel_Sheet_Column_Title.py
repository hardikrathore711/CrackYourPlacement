class Solution:
    def convertToTitle(self, cr: int) -> str:
        s = ""
        while cr//26>0:
            temp = cr%26
            if temp==0:
                temp=26
            s = chr(64+temp) + s
            if cr==26:
                cr=0
            elif cr%26==0:
                cr = (cr//26) -1
            else:
                cr = cr//26
            
        if cr>0:
            s = chr(64+cr) + s
        return s