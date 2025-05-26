
import math





class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        first = 1
        second = 1000000000

        while True:
            if first == second:
                return first
            mid = (first + second) // 2

            if self.loopAndFindPout(piles, mid, h) == True and (mid - 1 < 1 or self.loopAndFindPout(piles, mid - 1, h) == False):
                return mid
            elif self.loopAndFindPout(piles, mid, h) == True and (self.loopAndFindPout(piles, mid - 1, h) == True):
                second = mid - 1
            elif self.loopAndFindPout(piles, mid, h) == False and ( mid + 1 < 1000000001 and self.loopAndFindPout(piles, mid + 1, h) == False):
                first = mid + 1
            elif  self.loopAndFindPout(piles, mid, h) == False and (mid + 1 < 1000000001 and self.loopAndFindPout(piles, mid + 1, h) == True):
                return mid + 1

    def loopAndFindPout(self, piles, n, h):

        totalTime = 0

        for i in piles:
            
            ans = math.ceil(i / n)
            if ans <= 0:
                totalTime+= 1
            else:
                totalTime += ans
            if totalTime > h:
                return False
        # if totalTime <= h:
        #     print(n)
        #     print(totalTime)        
        return True