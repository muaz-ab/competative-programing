class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        current_min = float('-inf')
        for current_num in nums[::-1]:
            if current_num < current_min:
                return True
            while stack and stack[-1] < current_num:
                current_min = stack.pop()
            stack.append(current_num)

        return False