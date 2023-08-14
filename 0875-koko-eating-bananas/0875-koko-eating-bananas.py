import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # if len(piles) ==1 :
        #     return piles[0]
        piles.sort()
        # return piles
        max = piles[-1]
        min = 1

        ans = max

        while min <= max:
            # print(min, max)
            hours = 0
            mid = (max + min)//2
            for i in piles:
                hours += math.ceil(i/mid)
                if hours > h:
                    # max -= 1
                    min = mid + 1
                    break
            # if hours > h:

            if hours <= h:
                # min += 1
                max = mid - 1
                if ans > mid:
                    ans = mid
                # if

            # print(mid, ans)

        return ans
