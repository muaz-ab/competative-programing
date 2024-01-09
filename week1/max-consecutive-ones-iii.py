class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        window = []
        count = 0
        leng = 0
        for r in range(len(nums)):
            window.append(nums[r])
            if nums[r] == 0:
                count += 1
            while count > k:
                window.remove(nums[l])
                if nums[l] == 0:
                    count -= 1
                l += 1
            leng = max(leng , r -l + 1)
        return leng
