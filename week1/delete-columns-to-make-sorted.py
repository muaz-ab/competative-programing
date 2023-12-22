class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        for i, j in enumerate(zip(*strs)):
            if list(j) != sorted(list(j)):
                count += 1
            else:
                continue
        return count