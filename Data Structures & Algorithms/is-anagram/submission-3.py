class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):return False
        # creating a char array
        charArray=[0]*26
        n=len(s)

        # fill character array
        for i in range(n):
            charArray[ord(s[i])-ord('a')]+=1
            charArray[ord(t[i])-ord('a')]-=1

        # check if any location is non zero
        for ele in charArray:
            if ele!=0:
                return False
        return True 
        
        