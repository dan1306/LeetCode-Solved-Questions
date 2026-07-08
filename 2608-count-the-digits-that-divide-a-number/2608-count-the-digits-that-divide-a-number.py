class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        text = str(num)
        n = 0

        for i in text:
            if((num % (int(i))) == 0):
                n+=1
        return n
    