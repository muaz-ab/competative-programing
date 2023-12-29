class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x, y):
            return int(str(x) + str(y)) - int(str(y) + str(x))
        
        nums.sort(key=cmp_to_key(compare), reverse=True)
        result = ''.join(map(str, nums))   
        result = result.lstrip('0') or '0'

        return result