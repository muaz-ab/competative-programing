class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stk, L = [], len(nums)
        res = [-1] * L

        for i in range(L*2):
            idx = i % L
            while stk and nums[stk[-1]] < nums[idx]:
                res[stk.pop()] = nums[idx]
            stk.append(idx)
        return res