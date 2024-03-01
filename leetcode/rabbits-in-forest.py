class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        summ = 0
        for r , c in count.items():
            num = r + 1
            size = (c + num - 1) // num
            summ += num * size
        return summ
