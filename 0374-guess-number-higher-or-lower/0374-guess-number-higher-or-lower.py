# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        
        beg = 0
        end = n 

        mid =int(round((beg + end)/2))
        print(mid)

        while beg < end:

            if guess(mid) == 0:
                print(mid)
                return mid

            elif guess(mid) == -1:

                end = mid - 1
            else:

                beg = mid + 1

            mid = int(round((beg + end) / 2))


        if guess(mid) == 0:
            

            return mid
        
        
        """
        :type n: int
        :rtype: int
        """
        