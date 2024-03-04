class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        def win(l , r):
            if l > r:
                return 0
            winleft = nums[l] - win(l + 1, r)
            winright = nums[r] - win(l,r - 1)
            return max(winleft , winright)
        return win(0,n-1) >= 0