class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        result = []
        for i in range(len(boxes)):
            current = 0
            for j in range(len(boxes)):
                if int(boxes[j]) == 1:
                    current  += (abs(j - i))
            result.append(current)
        return result