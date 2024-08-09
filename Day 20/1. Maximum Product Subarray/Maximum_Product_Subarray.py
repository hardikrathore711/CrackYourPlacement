class Solution:
    def nikaloMax(self,lst,odd):
        ans = -float('inf')
        temp = 1
        if odd:
            hai1,hai2,hai3 = False,False,False
            temp2 = 1
            temp3 = 1
            i,j = 0,len(lst)-1
            while lst[i]>0:
                temp *= lst[i]
                i+=1
                hai1 = True
            if hai1:
                ans = max(ans,temp)
            pehla = lst[i]
            while lst[j]>0:
                temp3 *= lst[j]
                j-=1
                hai2 = True
            if hai2:
                ans = max(ans,temp3)
            aakhri = lst[j]
            i+=1
            while i<j:
                temp2 *= lst[i]
                i+=1
            ans = max(ans,temp*pehla*temp2)
            ans = max(ans,temp2*aakhri*temp3)
        else:
            for num in lst:
                temp*=num
            ans = max(ans,temp)
        return ans

    def maxProduct(self, nums):
        mp = -float('inf')
        for num in nums:
            mp = max(mp,num)
        temp = []
        neg = 0
        for num in nums:
            if num!=0:
                temp.append(num)
                if num<0:
                    neg+=1
            else:
                mp = max(mp,0)
                odd = (neg%2==1)
                if len(temp)>0:
                    mp = max(mp,self.nikaloMax(temp,odd))
                temp = []
                neg = 0
        odd = (neg%2==1)
        if len(temp)>0:
            mp = max(mp,self.nikaloMax(temp,odd))
        return mp