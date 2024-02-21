class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        window = []
        l = 0
        ans = float('inf')
        for i in range(len(blocks)):
            window += blocks[i]
            count = Counter(window)
            if len(window) == k and count['B'] == k:
                return 0
                break
            if len(window) == k:
                ans = min(ans,count['W'])
                window.remove(blocks[l])
                l += 1
        return ans if ans != float('inf') else 0
