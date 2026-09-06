class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) != len(t):
            return False

        a = self.returnDict(s)
        b = self.returnDict(t)

        for i in a:
            if i in b:
                if a[i] != b[i]:
                    return False
            else:
                return False
        
        return True
    
    def returnDict(self, n):
        a = {}

        for i in n:
            if i in a:
                a[i] += 1
            else:
                a[i] = 1

        return a
