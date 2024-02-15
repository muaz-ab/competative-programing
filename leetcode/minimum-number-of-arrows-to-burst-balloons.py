class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        curr = float('-inf')
        total = 0
        for start , end in points:
            if curr < start :
                curr = end
                total += 1
                
        return total