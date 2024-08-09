from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        dic = defaultdict(list)
        ans = []
        for s in strs:
            srt = sorted(s)
            st = "".join(srt)
            dic[st].append(s)
        for key in dic.keys():
            ans.append(dic[key])
        return ans