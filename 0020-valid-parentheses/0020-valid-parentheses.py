class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        container = []
        closed_breackets = ['}', ']', ')']
        open_brackets = {
            '{': 0,
            '[': 1,
            '(': 2 
        }
        for i in s:
            if i in closed_breackets:
                if len(container) == 0:
                    return False
                elif closed_breackets[open_brackets[container[len(container)- 1 ]]] == i:
                    container.pop(-1)
                else:
                    return False
            else:
                container.append(i)


        if len(container) == 0:
            return True
        else:
            return False

        