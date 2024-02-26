class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        odd_count = sum(1 for count in char_count.values() if count % 2 == 1)
        if odd_count <= 1:
            return len(s)
        else:
            return len(s) - odd_count + 1