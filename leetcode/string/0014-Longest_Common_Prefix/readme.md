# 14. Longest Common Prefix

## 문제

- 링크: https://leetcode.com/problems/longest-common-prefix/
- 난이도: Easy
- 태그: String, Trie

## 접근 방식

### Solution 1 — Prefix 축소 (startswith)

- 첫 번째 문자열을 prefix로 시작
- 각 문자열이 prefix로 시작하지 않으면 뒤에서 한 글자씩 잘라냄

### Solution 2 — Prefix 축소 (슬라이싱 비교)

- Solution 1과 같은 로직, `startswith` 대신 `string[:prefix_len]`으로 비교

### Solution 3 — 정렬 후 첫/끝 비교

- 사전순 정렬하면 가장 다른 두 문자열이 첫 번째와 마지막에 위치
- 이 둘만 비교하면 전체 공통 prefix를 구할 수 있음

## 풀이

### Solution 1

```python
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = strs[0]

        for string in strs:
            while not string.startswith(prefix):
                prefix = prefix[:-1]
                if prefix == "":
                    return ""

        return prefix
```

### Solution 2

```python
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
```

### Solution 3

```python
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
```

## 복잡도

|            | 시간            | 공간          |
| ---------- | --------------- | ------------- |
| Solution 1 | O(n \* m)       | O(1)          |
| Solution 2 | O(n \* m)       | O(1)          |
| Solution 3 | O(n \* m log n) | O(n) — 정렬용 |

- n: 문자열 개수, m: 가장 긴 문자열 길이

## 배운 점

- Solution 1·2는 prefix를 줄여가는 방식 — 같은 아이디어를 `startswith` vs 슬라이싱으로 표현
- Solution 3은 정렬 비용(O(n \* m log n))이 추가되지만, 비교를 두 문자열로 줄이는 발상이 독특
- 사전순 정렬에서 첫 번째와 마지막 문자열이 가장 차이가 크다는 성질을 활용
