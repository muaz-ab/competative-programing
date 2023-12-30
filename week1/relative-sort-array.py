class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)
        result = []
        for arr in arr2:
            result.extend([arr]*count[arr])
        dif = []
        for n in arr1:
            if n not in arr2:
                dif.append(n)
        dif.sort()
        result.extend(dif)
        return result