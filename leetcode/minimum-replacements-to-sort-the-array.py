class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        curr = nums[-1]
        ans = 0
        for i in range(len(nums)-1,-1,-1):
            if nums[i] <= curr:
                curr = nums[i]
                continue
            if nums[i] % curr == 0:
                res = nums[i]//curr
            else:
                res = nums[i]//curr + 1
                curr = nums[i]//res

            ans += res - 1
        return ans
        