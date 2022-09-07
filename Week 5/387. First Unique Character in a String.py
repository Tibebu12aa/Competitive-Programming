class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq_dict = {}
        for char in s:
            if char not in freq_dict:
                freq_dict[char] = 1
            else:
                freq_dict[char] = freq_dict[char] + 1
        for index in range(len(s)):
            if freq_dict[s[index]] == 1:
                return index
        return -1
    