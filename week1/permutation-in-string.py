class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        tar = list(s1[::-1])
        tar.sort()
        l = 0
        k = len(s1)
        window = []
        for r in range(len(s2)):
            window.append(s2[r])
            x =window
            x.sort()
            if x == tar:
                return True
            while len(window) >= k:
                window.remove(s2[l])
                l += 1
        return False