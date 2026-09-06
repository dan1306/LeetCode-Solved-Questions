class Solution(object):
    def lastStoneWeight(self, stones):

        while len(stones) > 1:

            f_max = max(stones)
            stones.remove(f_max)

            s_max = max(stones)
            stones.remove(s_max)

            if f_max == s_max:
                continue
            
            res = max(f_max, s_max) - min(f_max, s_max)
            stones.append(res)
        
        if len(stones) > 0:
            return stones[0]
        return 0
        """
        :type stones: List[int]
        :rtype: int
        """
        