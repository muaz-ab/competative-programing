class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l , h = 0 , len(nums) - 1
        while l < h:
            mid = (l + h) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                h = mid 
        return l if nums[l] == target else -1