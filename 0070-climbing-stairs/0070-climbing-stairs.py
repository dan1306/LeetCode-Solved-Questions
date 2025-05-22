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
            ans = 0
            incrementMe = 2
            while incrementMe < n:
                ans = first + sec

                first = sec
                sec = ans
                incrementMe += 1
            return ans

        