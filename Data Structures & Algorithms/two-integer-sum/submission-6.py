class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # using hashmap to store element with index
        map={}
        for idx,ele in enumerate(nums):
            rem=target-ele
            if rem in map:
                return [map[rem],idx]
            map[ele]=idx
        return [-1,-1]
        