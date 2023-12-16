class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = Counter(nums)
        for cu in count.keys():
            if count[cu] > 1:
                return cu