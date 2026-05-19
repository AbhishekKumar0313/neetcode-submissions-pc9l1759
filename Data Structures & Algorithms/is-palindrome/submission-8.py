class Solution:
    def check(self,ch):
        return 'A'<=ch<='Z' or 'a'<=ch<='z' or '0'<=ch<='9'
    def isPalindrome(self, s: str) -> bool:
        start,end=0,len(s)-1
        while start<=end:
            while start<end and  not self.check(s[start]):
                start+=1
            while start<end and not self.check(s[end]):
                end-=1
            if s[start].lower()!=s[end].lower():
                    return False
            start,end=start+1,end-1
        return True


        