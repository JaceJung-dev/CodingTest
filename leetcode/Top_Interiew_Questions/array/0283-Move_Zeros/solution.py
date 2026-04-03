class Solution:
    def moveZeros(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead
        """
        n = len(nums)
        write = 0

        for read in range(n):
            if nums[read] != 0:
                nums[write] = nums[read]
                write += 1

        for i in range(write, n):
            nums[i] = 0


class Solution2:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead
        """
        n = len(nums)
        write = 0

        for read in range(n):
            if nums[read] != 0:
                nums[read], nums[write] = nums[write], nums[read]
                write += 1
