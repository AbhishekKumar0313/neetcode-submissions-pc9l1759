class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate,vote=None,0
        for curr in nums:
            if vote==0:
                candidate=curr
            vote+=1 if candidate==curr else -1
        return candidate
        