class Solution:
    def intToRoman(self, num: int) -> str:
        s = ""
        dct = [["I","V","X"],["X","L","C"],["C","D","M"],["M","_","_"]]
        i = 0
        while num:
            unit = num%10
            num = num//10
            if unit>=5 and unit<9:
                s = (dct[i][1]) + (dct[i][0])*(unit-5) + s
            elif unit<4:
                s = (dct[i][0])*(unit) + s
            elif unit==4:
                s = (dct[i][0]) + (dct[i][1]) + s
            elif unit==9:
                s = (dct[i][0]) + (dct[i][2]) + s
            i+=1
        return s
        