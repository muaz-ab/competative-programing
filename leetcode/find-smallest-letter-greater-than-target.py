class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l , h = 0 , len(letters) - 1
        while l < h:
            mid = (h + l) // 2
            if letters[mid] > target:
                h = mid
            else:
                l = mid + 1
        return letters[l] if letters[l] > target else letters[0]