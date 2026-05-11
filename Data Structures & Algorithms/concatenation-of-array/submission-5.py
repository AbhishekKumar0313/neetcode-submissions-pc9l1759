class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n=len(nums)
        # create ans array
        ans=[0]*(2*n)
        # substitute values in ans
        for i,val in enumerate(nums):
            ans[i]=ans[i+n]=val
        return ans
        