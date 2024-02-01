class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)

        if n < 3 or arr[0] >= arr[1]:
            return False

        increasing = True

        for i in range(1, n):
            if increasing:
                if arr[i] == arr[i - 1]:
                    return False
                elif arr[i] < arr[i - 1]:
                    increasing = False
            else:
                if arr[i] >= arr[i - 1]:
                    return False

        return not increasing