class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # using set to check if element repeat or not in constant time because of hashing
        seen=set()
        for ele in nums:
            if ele in seen:
                return True
            seen.add(ele)
        return False
        