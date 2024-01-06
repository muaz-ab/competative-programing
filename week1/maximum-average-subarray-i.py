class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sli_window = nums[:k]
        curr = sum(sli_window)
        max_ave = curr
        for i in range(k,len(nums)):
            curr -= nums[i-k]
            curr += nums[i]
            max_ave = max(max_ave , curr)
        return max_ave/k