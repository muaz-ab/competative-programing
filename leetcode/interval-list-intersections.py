class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        comb = firstList + secondList
        comb.sort()
        res = []
        l , r = 0 , 0
        n , m = len(firstList) , len(secondList)
        while l < n and r < m:
            li1 = max(firstList[l][0],secondList[r][0])
            li2 = min(firstList[l][1],secondList[r][1])
            if li1 <= li2:
                res.append([li1,li2])
            if firstList[l][1] < secondList[r][1]:
                l += 1
            else:
                r += 1
        return res
