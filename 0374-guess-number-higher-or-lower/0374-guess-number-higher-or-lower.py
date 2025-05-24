# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        first = 1
        second = n



        while True:
            mid = (first + second) / 2
            ans = guess(mid)

            
            if first == second:
                return first
            elif ans == 0:
                return mid
            elif ans == -1:
                second = mid - 1
            else:
                first = mid + 1
        