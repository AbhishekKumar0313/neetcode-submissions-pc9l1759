class Solution:
    def isPalindrome(self, s: str) -> bool:
        # function to check special character
        def check(ch):
            return (('a' <= ch <= 'z') or ('A' <= ch <= 'Z') or
            ('0' <= ch <= '9'))

        # setting corners
        left,right=0,len(s)-1
        # checking from both sides
        while left<right:
            while left<right and not check(s[left]):
                left+=1
            while left<right and not check(s[right]):
                right-=1
            if left<right and s[left].lower()!=s[right].lower():
                return False
            left,right=left+1,right-1
        return True

        
            