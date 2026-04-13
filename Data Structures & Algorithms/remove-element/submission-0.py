class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        stick,move,n=0,0,len(nums)
        while move<n:
            if nums[move]!=val:
                nums[stick],nums[move]=nums[move],nums[stick]
                stick,move=stick+1,move+1
            else:
                move+=1
        return stick

        