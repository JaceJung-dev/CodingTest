from collections import Counter


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result = []
        count = Counter(nums1)

        for num in nums2:
            if count[num] > 0:
                result.append(num)
                count[num] -= 1

        return result


class Solution2:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1.sort()
        nums2.sort()

        result = []
        i, j = 0, 0
        len_nums1, len_nums2 = len(nums1), len(nums2)
        while i < len_nums1 and j < len_nums2:
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                result.append(nums1[i])
                i += 1
                j += 1

        return result
