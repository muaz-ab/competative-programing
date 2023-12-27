class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        i = [0]*len(nums)
        k = [0]*len(nums)
        min_ind = float('inf')
        max_ind = float('-inf')
        for n in range(len(nums)):
            if n == 0:
                continue
            elif nums[n - 1] < min_ind:
                min_ind = nums[n-1]
            i[n] = min_ind
            le = len(nums) - n -1
            if le == len(nums)-1:
                continue
            elif nums[le+1] > max_ind:
                max_ind = nums[le+1]
            k[le+1] = max_ind
        for idx in range(len(nums)):
            if (nums[idx] > i[idx])  and (nums[idx] < k[idx]):
                return True
        return False