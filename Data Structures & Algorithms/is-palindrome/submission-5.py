class Solution:
    def checkIsAlnum(self,ch) -> bool:
        return (
            ('A' <= ch <= 'Z') or 
            ('a' <= ch <= 'z') or 
            ('0' <= ch <= '9')
        )
    def isPalindrome(self, s: str) -> bool:
        left,right=0,len(s)-1
        while left<right:
            while left<right and not self.checkIsAlnum(s[left]):
                left+=1
            while left<right and not self.checkIsAlnum(s[right]):
                right-=1
            if left<=right and s[left].lower()!=s[right].lower():
                return False
            left,right=left+1,right-1
        return True
            


        