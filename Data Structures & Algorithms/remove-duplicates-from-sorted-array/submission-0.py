class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if not nums:
            return 0

        unique_index = 0

        for move in range(1, len(nums)):

            if nums[move] != nums[unique_index]:
                unique_index += 1
                nums[unique_index] = nums[move]

        return unique_index + 1