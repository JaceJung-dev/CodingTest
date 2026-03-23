class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums_set = set(nums)
        if len(nums) != len(nums_set):
            return True
        else:
            return False


class Solution2:
    def containsDuplicate(self, nums: list[int]) -> bool:
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return True

        return False


class Solution3:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        n = len(nums)

        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                return True

        return False


class Solution4:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)

        return False


class Solution5:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = {}

        for num in nums:
            if num in seen and seen[num] >= 1:
                return True
            else:
                seen[num] = seen.get(num, 0) + 1

        return False
