class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res = 0
        for i in nums:
            if i % 2 == 0:
                res += i 
        ansr = []
        for q in queries:
            if nums[q[1]] % 2 == 0:
                res -= nums[q[1]]
            nums[q[1]] += q[0]
            if nums[q[1]] % 2 == 0:
                res += nums[q[1]]
            ansr.append(res)
        return ansr