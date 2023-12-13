class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        val = abs(target[0]) + abs(target[1])
        t = []
        for i in range(len(ghosts)):
            path = [abs(ghosts[i][0]-target[0]),abs(ghosts[i][1]-target[1])]
            if sum(path) <= val:
                return False
        return True
        