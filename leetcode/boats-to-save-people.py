class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        cnt, left, right = 0, 0, len(people) - 1

        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            cnt, right = cnt + 1, right - 1

        return cnt