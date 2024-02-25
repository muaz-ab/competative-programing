class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        pre = defaultdict(int)
        summ = curr = 0
        pre[curr] = 1
        for num in nums:
            curr += num
            summ += pre[curr-goal]
            pre[curr] += 1
        return summ

        
        