class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        l , r = 0 , len(skill) - 1
        ans , summ = 0 , 0 
        skill.sort()
        for i in range(len(skill)//2):
            if i == 0:
                summ += (skill[l] + skill[r])
                ans += (skill[l] * skill[r])
            else:
                if summ != skill[l] + skill[r]:
                    return -1
                else:
                    ans += (skill[l] * skill[r])
            l += 1
            r -= 1
        return ans