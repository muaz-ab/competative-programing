class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        rem = sum(nums) % p
        if rem == 0:
            return 0
        mod_indices = {0: -1}
        curr = 0
        min_length = len(nums)
        for i , num in enumerate(nums):
            curr = (curr + num) % p
            target_mod = (curr - rem + p) % p
            if target_mod in mod_indices:
                min_length = min(min_length, i - mod_indices[target_mod])
            mod_indices[curr] = i
        return -1 if min_length == len(nums) else min_length

            