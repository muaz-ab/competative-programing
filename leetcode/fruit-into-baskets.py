class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        cont = collections.defaultdict(int)
        l , total , ans = 0 , 0 , 0
        for r in range(len(fruits)):
            cont[fruits[r]] += 1
            total += 1
            while len(cont) > 2:
                f = fruits[l]
                cont[f] -= 1
                total -= 1
                l += 1
                if cont[f] == 0:
                    cont.pop(f)

            ans = max(ans, total)

        return ans