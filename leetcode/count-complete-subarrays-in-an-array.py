class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        count = len(set(nums))
        res = 0
        for i in range(len(nums)):
            window = set()
            for j in range(i,len(nums)):
                window.add(nums[j])
                if len(window) == count:
                    res += 1
                elif len(window) > count:
                    break
        return res
