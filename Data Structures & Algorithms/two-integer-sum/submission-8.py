class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map={}
        for idx,val in enumerate(nums):
            rem=target-val
            if rem in map:
                return [map[rem],idx]
            map[val]=idx
        return [-1,-1]
        