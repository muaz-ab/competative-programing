class Solution:
    def reverseWords(self, s: str) -> str:
        result =""
        container = s.split()
        for i in range(len(container)):
            result = result + " " + container[len(container)-i-1]
        return result.strip()