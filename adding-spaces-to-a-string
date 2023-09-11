class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        arr = []
        prev = 0
        for i in spaces:
            arr.append(s[prev:i])
            prev = i
        arr.append(s[i:])
        return " ".join(arr)
