class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = strs[0]
        for word in strs[1:]:
            i = 0
            till = min(len(word),len(common))
            while i<till:
                if common[i]==word[i]:
                    i+=1
                else:
                    break
            common = common[:min(i,till)]
            if common=="":
                break
        return common