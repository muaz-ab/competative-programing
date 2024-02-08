class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        summ = 0
        prefixsum = [0]
        for i in range(len(nums)):
            summ += nums[i]
            prefixsum.append(summ)
        pre = {}
        count =0
        for i in range(len(prefixsum)):
             x = prefixsum[i] - k
             if x in pre:
                count += pre[x]

             if prefixsum[i] in pre:
                pre[prefixsum[i]] += 1
             else:
                pre[prefixsum[i]] = 1

        return count
        