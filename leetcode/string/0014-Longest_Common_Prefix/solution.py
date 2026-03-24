class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = strs[0]

        for string in strs:
            while not string.startswith(prefix):
                prefix = prefix[:-1]
                if prefix == "":
                    return ""

        return prefix


class Solution2:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = strs[0]
        prefix_len = len(prefix)

        for string in strs[1:]:
            while prefix != string[:prefix_len]:
                prefix_len -= 1
                if prefix_len == 0:
                    return ""

                prefix = prefix[:prefix_len]

        return prefix


class Solution3:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ""
        sorted_list = sorted(strs)
        for i in range(len(sorted_list[0])):
            if sorted_list[0][i] != sorted_list[-1][i]:
                return prefix
            else:
                prefix += sorted_list[0][i]
        return prefix
