class Solution(object):
    def climbStairs(self, n):

        if n == 1:
            return 1

        arr = [1, 1]

        for i in range(0, n - 1):

            arr.append( arr[-1] + arr[-2])

        return(arr[-1])