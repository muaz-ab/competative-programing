class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = float('inf')
        for i in range(len(nums)):
            j , k = i + 1 , len(nums) - 1
            while j < k:
                summ = nums[i] + nums[j] + nums[k]
                if summ == target:
                    return summ
                if abs(summ - target) < abs(ans - target):
                    ans = summ
                if summ > target:
                    k -= 1
                else:
                    j += 1
        return ans if ans != float('inf') else 0