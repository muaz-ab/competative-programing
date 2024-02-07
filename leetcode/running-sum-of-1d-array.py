class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        summ = 0
        cont = []
        for i in range(len(nums)):
            summ += nums[i]
            cont.append(summ)
        return cont