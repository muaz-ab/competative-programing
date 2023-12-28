class Solution:
    def sortSentence(self, s: str) -> str:
        container = list(s.split())
        container.sort(key = lambda a:a[-1])
        result = ""
        for chx in container:
            result += chx[:-1] +" " 

        return result.strip()