class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totmul = 1
        totzer = 1
        answer = []
        for i in range(len(nums)):
            if nums[i] != 0:
                totmul = totmul*nums[i]
                totzer = totzer*nums[i]
            else:
                totzer = totmul
                totmul = totmul*nums[i]
        for j in range(len(nums)):
            if nums[j] != 0:
                answer.append(totmul//nums[j])
            else:
                answer.append(totzer)
        return answer