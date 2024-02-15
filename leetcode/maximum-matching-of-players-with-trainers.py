class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        l , r = 0 , 0
        players.sort()
        trainers.sort()
        while l < len(players) and r < len(trainers):
            if players[l] <= trainers[r]:
                l += 1
            r += 1
        return l