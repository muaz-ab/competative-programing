class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = n
        while True:
            if num % 2 == 0 and num % n == 0:
                return num
            num += n
            