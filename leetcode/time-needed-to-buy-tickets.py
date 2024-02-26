class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        q = deque(range(n))
        time = 0

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                tickets[node] -= 1

                if tickets[node] >= 1:
                    q.append(node)

                time += 1
                if tickets[k] == 0:
                    return time