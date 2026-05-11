class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if not of same length -> reject
        if len(s)!=len(t):
            return False
        # creating character map
        charMap=[0]*26
        n=len(s)
        for i in range(n):
            charMap[ord(s[i])-97]+=1
            charMap[ord(t[i])-97]-=1
        # check if any non zero value
        for ele in charMap:
            if ele!=0:
                return False
        return True
            
        
        