# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        first = 1
        second = n


        while True:
            if first == second:
                return first
            mid = (first + second) // 2

            if isBadVersion(mid) == True and ((isBadVersion(mid - 1) == False) or (mid - 1 < 1)):
                return mid
            elif isBadVersion(mid) == False:
                first = mid + 1
            elif isBadVersion(mid) == True and isBadVersion(mid - 1) == True :
                second = mid - 1


        
        