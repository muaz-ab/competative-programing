from collections import Counter
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        threshold = n // 4

        current_element = arr[0]
        count = 1
        if len(arr) == 1:
            return arr[0]

        for i in range(1, n):
            if arr[i] == current_element:
                count += 1
                if count > threshold:
                    return current_element
            else:
                current_element = arr[i]
                count = 1

        return -1 