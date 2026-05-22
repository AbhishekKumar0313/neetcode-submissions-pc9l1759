from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap=defaultdict(list)
        for string in strs:
            counter=[0]*26
            for ch in string:
                counter[ord(ch)-ord('a')]+=1
          
            hashmap[tuple(counter)].append(string)
        return list(hashmap.values())
        