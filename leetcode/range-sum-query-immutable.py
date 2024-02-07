class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixsum = []
        summ = 0
        for i in range(len(nums)):
            summ += nums[i]
            self.prefixsum.append(summ)


    def sumRange(self, left: int, right: int) -> int:
        rightsum = self.prefixsum[right]
        if left > 0:
            leftsum = self.prefixsum[left - 1]
        else:
            leftsum = 0
        return rightsum - leftsum

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)