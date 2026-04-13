class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):return False
        charmap=[0]*26
        n=len(s)
        for i in range(n):
            charmap[ord(s[i])-97]+=1
            charmap[ord(t[i])-97]-=1
        
        for i in charmap:
            if i!=0:
                return False
        return True
        

        