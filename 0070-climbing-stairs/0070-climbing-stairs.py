class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            first = 1
            sec = 2
            incrementMe = 2
            while incrementMe < n:
                dummy = sec
                sec  = first + sec
                first = dummy
                incrementMe += 1
            return sec

        