class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        maxx = 0
        res = {}
        countl = 0
        countr = Counter(nums)
        countr = countr[1]
        
        for i in range(len(nums)):
            score = countl + countr
            if score not in res:
                res[score] = [i]
            else:
                res[score] += [i]
            if nums[i] == 0:
                countl += 1
            if nums[i] == 1:
                countr -= 1
            k = i
        score = countl + countr
        if score not in res:
            res[score] = [k+1]
        else:
            res[score] += [k+1]   
        ret = max(res)
        return res[ret]
