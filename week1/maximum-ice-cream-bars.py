class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        count = 0
        costs.sort()
        summ = 0
        for cost in costs:
            summ += cost
            if summ <= coins:
                count += 1
            else:
                break
        return count