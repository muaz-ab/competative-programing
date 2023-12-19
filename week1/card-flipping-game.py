class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        cont = set()
        for front , back in zip(fronts, backs):
            if front == back :
                cont.add(front)
        
        res = inf
        for card in fronts + backs:
            if card not in cont :
                res = min(res , card)
        return res if res != inf else 0