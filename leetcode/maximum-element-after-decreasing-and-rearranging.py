class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        curr = arr[0]
        if curr != 1:
            curr = 1
        for i in range(1,len(arr)):
            if arr[i] - curr > 1:
                curr = curr + 1
            else:
                curr = arr[i]
        return curr