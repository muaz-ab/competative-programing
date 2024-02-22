class Solution:
    def maxScore(self, cardpoints: List[int], k: int) -> int:
        len_window = len(cardpoints) - k
        window_l = cardpoints[:len_window]
        current_sum = sum(window_l)
        min_sum = current_sum
        total_sum = sum(cardpoints)
        for i in range(len(cardpoints) - len_window ):
            current_sum = current_sum + cardpoints[i + len_window] - cardpoints[i]
            min_sum = min(min_sum , current_sum)
        return total_sum - min_sum
