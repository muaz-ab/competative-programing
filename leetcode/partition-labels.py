class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lsindx = {}
        for i , c in enumerate(s):
            lsindx[c] = i
        res = []
        size , end = 0 , 0
        for i , c in enumerate(s):
            size += 1
            end = max(end,lsindx[c])
            if end == i:
                res.append(size)
                size = 0
        return res 