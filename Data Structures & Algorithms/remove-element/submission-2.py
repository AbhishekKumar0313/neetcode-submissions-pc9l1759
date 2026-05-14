class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # use two pointer - one to move and other to replace
        move,static=0,0
        while move<len(nums):
            if nums[move]!=val:
                nums[move],nums[static]=nums[static],nums[move]
                static+=1
            move+=1
        return static


        