class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        l = 0
        window = {}
        res = float('inf')
        for r in range(len(cards)):
            if cards[r] not in window:
                window[cards[r]] = 1
            else:
                window[cards[r]] += 1
            if window[cards[r]] >= 2:
                while cards[r] != cards[l]:
                    window[cards[l]] -= 1
                    l += 1
                res = min(res,r-l+1)
                window[cards[l]] -= 1
                l += 1
        return res if res != float('inf') else -1
