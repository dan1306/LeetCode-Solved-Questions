class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        string_a = {}
        string_b = {}
        
#         if len(string_a) is not len(string_b):
#             return string_b[-1]

        for i in s:
            if i in string_a:
                string_a[i] += 1
            else:
                string_a[i] = 1
        for i in t:
            if i in string_b:
                string_b[i] += 1
            else:
                string_b[i] = 1
                
        for i in string_b:
            if i not in string_a:
                return i
            elif string_b[i] is not string_a[i]:
                return i
