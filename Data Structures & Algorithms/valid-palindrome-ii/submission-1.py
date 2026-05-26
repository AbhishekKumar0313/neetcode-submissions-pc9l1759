class Solution:
    def validPalindrome(self, s: str) -> bool:
        start,end=0,len(s)-1
        while start<end:
            if s[start]!=s[end]:
                print(start,end,s[start+1:end+1],s[end:start:-1],s[start:end],s[end-1:start-1:-1])
                return s[start+1:end+1]==s[end:start:-1] or s[start:end]==s[end-1:start-1:-1]
            start,end=start+1,end-1
        return True

    
        
        
        





        