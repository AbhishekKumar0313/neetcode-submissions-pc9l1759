class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n=len(nums)
        
        # creating container
        ans=[0]*(2*n)

        # putting values
        for idx,val in enumerate(nums):
            ans[idx]=ans[idx+n]=val
        
        return ans
        