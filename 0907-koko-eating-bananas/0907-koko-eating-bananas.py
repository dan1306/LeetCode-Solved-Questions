class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        l, r = 1, max(piles)
        returnMe = r


        while l <= r:
            mid = (l + r) // 2
            # print(mid)
            hoursInFeed = 0
            for i in piles:
                # print(mid, math.ceil(i / mid))
                # hoursInFeed = i // mid
                hoursInFeed += (i + mid - 1) // mid
    
            
            if hoursInFeed <= h and mid < returnMe:
                returnMe = mid
            
            if hoursInFeed > h:
                l = mid + 1
            else:
                r = mid - 1
        
        return returnMe
            