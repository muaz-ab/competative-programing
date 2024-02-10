class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        summ = 0
        pre = {0:1}
        count =0
        for i in range(len(nums)):
            summ += nums[i]
            x = summ % k
            if x in pre:
                count += pre[x]

            if x in pre:
                pre[x] += 1
            else:
                pre[x] = 1
        return count