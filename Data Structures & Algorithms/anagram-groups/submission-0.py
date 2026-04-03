from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for s in strs:
            string="".join(sorted(s))
            res[string].append(s)
        return list(res.values())
