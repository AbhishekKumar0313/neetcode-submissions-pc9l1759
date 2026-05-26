class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word=[]
        idx=0
        while idx<len(word1) or idx <len(word2) :
            if idx<len(word1) : word.append(word1[idx])
            if idx<len(word2) : word.append(word2[idx])
            idx+=1

        return ''.join(word)