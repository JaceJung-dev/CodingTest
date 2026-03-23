class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return []


class Solution2:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        num_map = {}

        for i in range(n):
            num_map[nums[i]] = i

        for i in range(n):
            complement = target - nums[i]
            if complement in num_map and num_map[complement] != i:
                return [i, num_map[complement]]

        return []


class Solution3:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i

        return []
