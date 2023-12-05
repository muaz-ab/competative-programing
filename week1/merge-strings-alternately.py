class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        leng = min(len(word1) , len(word2))
        container = ""
        for i in range(leng):
            container += word1[i]
            container += word2[i]
            if i == leng - 1 and len(word1) > len(word2):
                container += word1[i+1:]
                return container
            if i == leng - 1 and len(word2) > len(word1):
                container += word2[i+1:]
                return container
        return container