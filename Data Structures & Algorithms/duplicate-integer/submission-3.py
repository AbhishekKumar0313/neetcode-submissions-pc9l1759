class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # create a set
        seen=set()

        # iterate and check if it comes earlier
        for ele in nums:
            if ele in seen:
                return True
            seen.add(ele)
        return False
        
        