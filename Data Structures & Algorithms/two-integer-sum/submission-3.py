class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for idx,ele in enumerate(nums):
            rem=target-ele
            if rem in hashmap:
                return [hashmap[rem],idx]
            hashmap[ele]=idx
        return [-1,-1]
        