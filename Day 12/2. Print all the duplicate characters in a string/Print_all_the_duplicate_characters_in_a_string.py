class Solution:
    def printDuplicates(self,str):
        dic = {}
        for i in range(len(str)):
            dic[str[i]] = dic.get(str[i],0) + 1
        for key in dic.keys():
            if dic[key] > 1:
                print(f"{key}, count={dic[key]}")
S = input()
obj = Solution()
obj.printDuplicates(S)