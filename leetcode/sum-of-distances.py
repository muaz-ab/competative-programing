class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            if num not in d:
                d[num] = []
            d[num].append(i)
        answer = [0] * len(nums)
        for num, indices in d.items():
            suffix_sum = sum(indices)
            prefix_sum = 0
            suffix_len = len(indices)
            prefix_len = 0
            for i in indices:
                prefix_sum += i
                prefix_len += 1
                suffix_sum -= i
                suffix_len -= 1
                answer[i] = -prefix_sum + prefix_len * i - suffix_len * i + suffix_sum
        return answer