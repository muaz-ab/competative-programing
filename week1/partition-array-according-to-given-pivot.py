class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lowe = []
        equ = []
        hig = []
        for num in nums:
            if num < pivot:
                lowe.append(num)
            if num == pivot:
                equ.append(num)
            if num > pivot:
                hig.append(num)
        return lowe + equ + hig