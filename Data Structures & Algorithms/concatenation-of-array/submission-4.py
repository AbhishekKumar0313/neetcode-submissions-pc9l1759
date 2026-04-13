class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[0]*(2*n)
        for idx,ele in enumerate(nums):
            ans[idx]=ans[idx+n]=ele
        return ans
        


        