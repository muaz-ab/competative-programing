class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        ans = []
        for count in counter.keys():
            if counter[count] > len(nums)//3:
                ans.append(count)
        return ans