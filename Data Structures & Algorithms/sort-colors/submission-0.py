class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left,right,move=0,len(nums)-1,0
        while move<=right:
            if nums[move]==0:
                nums[left],nums[move]=nums[move],nums[left]
                left,move=left+1,move+1
            elif nums[move]==2:
                nums[move],nums[right]=nums[right],nums[move]
                right-=1
            else:
                move+=1
        

