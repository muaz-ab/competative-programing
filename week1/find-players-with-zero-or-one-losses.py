class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players = set()
        losses = collections.Counter()
        for win , loser in matches:
            losses[loser] += 1
            players.add(win)
            players.add(loser)
        no_lose , one_lose = [] , []
        for player in players:
            if losses[player] == 0:
                no_lose.append(player)
            elif losses[player] == 1:
                one_lose.append(player)
        return [sorted(no_lose) , sorted(one_lose)]