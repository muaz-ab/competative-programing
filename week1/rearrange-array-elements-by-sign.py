class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        result = []
        pos , neg = [] , []
        if len(nums) == 2:
            if nums[0] > nums[1]:
                return [nums[0],nums[1]]
            else:
                return [nums[1],nums[0]]
        for num in nums:
            if num >= 0:
                pos.append(num)
            else:
                neg.append(num)
        numm = pos + neg
        n = len(numm)//2
        for i in range(len(numm)-n):
            result.append(numm[i])
            result.append(numm[i+n])
        return result