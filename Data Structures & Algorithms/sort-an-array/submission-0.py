from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def heapify_down(idx, size):
            largest = idx
            left = 2*idx + 1
            right = 2*idx + 2

            if left < size and nums[left] > nums[largest]:
                largest = left

            if right < size and nums[right] > nums[largest]:
                largest = right

            if largest != idx:
                nums[largest], nums[idx] = nums[idx], nums[largest]
                heapify_down(largest, size)

        def heap_sort():
            n = len(nums)

            for i in range(n//2 - 1, -1, -1):
                heapify_down(i, n)
            print(nums)

            for i in range(n-1, 0, -1):
                nums[0], nums[i] = nums[i], nums[0]
                heapify_down(0, i)   

        heap_sort()
        return nums