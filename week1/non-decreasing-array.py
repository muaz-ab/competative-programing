class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = False
        for i in range(len(nums)-1):
            if nums[i] <= nums[i + 1]:
                continue
            elif count == True:
                return False
            
            if i == 0 or nums[i - 1] <= nums[i + 1]:
                nums[i] = nums[i+1]
            else:
                nums[i+1] = nums[i]
            count = True
        return True